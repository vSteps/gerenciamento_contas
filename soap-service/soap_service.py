from spyne import Application, rpc, ServiceBase, Integer, Decimal
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server

# Defina o serviço SOAP
class AccountService(ServiceBase):
    @rpc(Integer, _returns=Decimal)
    def get_account(ctx, user_id):
        # Simula saldo com base no user_id
        return {
            1: 1500.50,
            2: 2500.00
        }.get(user_id, 0.0)

# Crie a aplicação SOAP
application = Application(
    [AccountService],  # Lista de serviços
    tns='spyne.examples.account',  # Namespace
    in_protocol=Soap11(validator='lxml'),  # Protocolo de entrada
    out_protocol=Soap11()  # Protocolo de saída
)

# Crie o servidor WSGI
wsgi_application = WsgiApplication(application)

# Inicie o servidor
if __name__ == '__main__':
    server = make_server('0.0.0.0', 8002, wsgi_application)
    print("SOAP service running on http://localhost:8002")
    server.serve_forever()