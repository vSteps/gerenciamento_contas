package com.exemplo;

import javax.xml.namespace.QName;
import javax.xml.ws.Service;
import java.net.URL;

public class AccountClient {
    public static void main(String[] args) {
        try {

            URL wsdlUrl = new URL("http://localhost:8002/soap/account?wsdl");


            QName serviceName = new QName("spyne.examples.account", "AccountService");

 
            Service service = Service.create(wsdlUrl, serviceName);

            AccountService port = service.getPort(AccountService.class);

            double balance = port.getAccount(1);
            System.out.println("Saldo da conta: " + balance);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}