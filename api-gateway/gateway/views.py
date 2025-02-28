from rest_framework.decorators import api_view # type: ignore
from rest_framework.response import Response # type: ignore
import requests # type: ignore
from spyne.client.http import HttpClient
from spyne.protocol.soap import Soap11
from zeep import Client as ZeepClient # type: ignore

@api_view(['GET', 'POST'])  # Adicionei POST
def users(request):
    if request.method == 'POST':
        response = requests.post('http://localhost:8001/api/users/', data=request.data)
        return Response(response.json(), status=response.status_code)
    
    response = requests.get('http://localhost:8001/api/users/')
    data = {
        'users': response.json(),
        'links': [
            {'rel': 'self', 'href': 'http://localhost:8000/gateway/users'},
            {'rel': 'account', 'href': 'http://localhost:8000/gateway/account/1'}
        ]
    }
    return Response(data)
@api_view(['GET'])
def account(request, user_id):
    wsdl_url = 'http://localhost:8002/soap/account?wsdl'
    
    # Crie o cliente SOAP com Zeep
    client = ZeepClient(wsdl_url)
    
    # Chame o método diretamente
    result = client.service.get_account(user_id)
    
    return Response({
        'balance': result,
        'links': [
            {'rel': 'self', 'href': f'http://localhost:8000/gateway/account/{user_id}'},
            {'rel': 'users', 'href': 'http://localhost:8000/gateway/users'}
        ]
    })