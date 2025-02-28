@echo off
start "API Gateway" cmd /k "cd api-gateway && .\venv\Scripts\activate && python manage.py runserver 8000"
start "Serviço REST" cmd /k "cd rest-service && .\venv\Scripts\activate && python manage.py runserver 8001"
start "Serviço SOAP" cmd /k "cd soap-service && .\venv\Scripts\activate && python soap_service.py"
start "Cliente Angular" cmd /k "cd angular-client && npm install && ng serve"
echo Todos os serviços estão rodando!
pause