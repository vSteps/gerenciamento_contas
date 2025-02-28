from spyne import Application, rpc, ServiceBase, Integer, Decimal
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server


class AccountService(ServiceBase):
    @rpc(Integer, _returns=Decimal)
    def get_account(ctx, user_id):

        return {
            1: 1500.50,
            2: 2500.00
        }.get(user_id, 0.0)


application = Application(
    [AccountService], 
    tns='spyne.examples.account',  
    in_protocol=Soap11(validator='lxml'),  
    out_protocol=Soap11()  
)


wsgi_application = WsgiApplication(application)


if __name__ == '__main__':
    server = make_server('0.0.0.0', 8002, wsgi_application)
    print("SOAP service running on http://localhost:8002")
    server.serve_forever()