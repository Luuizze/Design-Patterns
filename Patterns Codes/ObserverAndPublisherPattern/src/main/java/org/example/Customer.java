package org.example;

public class Customer implements Observer {
    private String name;

    public Customer(String name, OnlineStore store) {
        this.name = name;
        store.registerObserver(this);  // Registro automático do cliente na loja
    }
    @Override
    public void update(String product) {
        System.out.println("Olá " + name + ", o produto " + product + " está em promoção!");
    }
}
