# Sistema de Gerenciamento de Contas Online

Este projeto implementa uma arquitetura que integra serviços REST e SOAP, utilizando um API Gateway como ponto central de comunicação. O sistema permite gerenciar usuários e consultar saldos de contas.

## Arquitetura

- **API Gateway (Django, porta 8000):** Roteia requisições para serviços REST e SOAP, implementa HATEOAS e fornece documentação via Swagger.
- **Serviço REST (Django, porta 8001):** Gerencia usuários (CRUD).
- **Serviço SOAP (Python/Spyne, porta 8002):** Disponibiliza saldo da conta.
- **Cliente Angular (porta 4200):** Interface para interagir com o sistema.

## Como Executar

### Pré-requisitos
- Python 3.11
- Node.js (para o Angular)
- Git

### Passos

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/vsteps/gerenciamento_contas.git
   ```
2. **Rode a API Gateway**
    ```bash
    cd api-gateway
    python -m venv venv
    .\venv\Scripts\activate
    pip install -r requirements.txt
    ```
3. **Rode o Serviço REST**
    ```bash
    cd rest-service
    python -m venv venv
    .\venv\Scripts\activate
    pip install -r requirements.txt
    ```
4. **Rode o Serviço SOAP**
    ```bash
    cd soap-service
    python -m venv venv
    .\venv\Scripts\activate
    pip install -r requirements.txt
    ```
5. **Rode o Cliente Angular**
    ```bash
    cd angular-client
    npm install  
    ```
5. **Rode todos os processos com o arquivo.bat**
    ```bash
    cd ..
    (verifique que voce se encontra no diretório raiz do projeto: gerenciamento_contas/)
    .\run-all.bat
    ```
## Endpoints
- API Gateway: http://localhost:8000

- Swagger UI: http://localhost:8000/swagger/

- Serviço REST: http://localhost:8001/api/users/

- Serviço SOAP (WSDL): http://localhost:8002/soap/account?wsdl

- Cliente Angular http://localhost:4200

## Exemplos de Uso
### Criar usuário Angular

1.  Acesse http://localhost:4200
2.  Preencha o formulário e clique em "Criar usuário"

### Consultar Saldo(Java)

Execute o cliente Java para consultar o saldo:

Para isso, acesse o arquivo AccountClient.java e clique em "Run"