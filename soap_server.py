from spyne import Application, rpc, ServiceBase, Unicode, ByteArray, Iterable
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
import os

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

class FileTransferService(ServiceBase):
    
    @rpc(Unicode, ByteArray, _returns=Unicode)
    def upload_file(ctx, filename, file_data):
        """Recebe um arquivo e o salva no servidor"""
        file_path = os.path.join(UPLOAD_DIR, filename)
        with open(file_path, "wb") as f:
            f.write(file_data)
        return f"Arquivo '{filename}' recebido com sucesso!"
    
    @rpc(_returns=Iterable(Unicode))
    def list_files(ctx):
        """Lista os arquivos disponíveis no servidor"""
        return os.listdir(UPLOAD_DIR)
    
    @rpc(Unicode, _returns=ByteArray)
    def download_file(ctx, filename):
        """Retorna o conteúdo de um arquivo solicitado"""
        file_path = os.path.join(UPLOAD_DIR, filename)
        if os.path.exists(file_path):
            with open(file_path, "rb") as f:
                return f.read()
        raise ValueError(f"Arquivo '{filename}' não encontrado!")

# Configurar a aplicação SOAP
application = Application(
    [FileTransferService],
    "filetransfer.soap",
    in_protocol=Soap11(validator="lxml"),
    out_protocol=Soap11()
)

# Criar o servidor WSGI
if __name__ == "__main__":
    from wsgiref.simple_server import make_server
    wsgi_app = WsgiApplication(application)
    server = make_server("0.0.0.0", 8000, wsgi_app)
    print("Servidor SOAP rodando em http://0.0.0.0:8000")
    server.serve_forever()
