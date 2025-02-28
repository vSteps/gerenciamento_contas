package com.exemplo;

import javax.xml.namespace.QName;
import javax.xml.ws.Service;
import java.net.URL;

public class AccountClient {
    public static void main(String[] args) {
        try {
            // URL do WSDL
            URL wsdlUrl = new URL("http://localhost:8002/soap/account?wsdl");

            // Nome do serviço e namespace (verifique no WSDL)
            QName serviceName = new QName("spyne.examples.account", "AccountService");

            // Criar o serviço
            Service service = Service.create(wsdlUrl, serviceName);

            // Obter a porta do serviço
            AccountService port = service.getPort(AccountService.class);

            // Chamar o método SOAP
            double balance = port.getAccount(1);
            System.out.println("Saldo da conta: " + balance);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}