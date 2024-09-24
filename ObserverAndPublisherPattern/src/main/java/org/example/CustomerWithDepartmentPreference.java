package org.example;

public class CustomerWithDepartmentPreference implements Subscriber {
    private String name;

    public CustomerWithDepartmentPreference(String name, OnlineStoreWithDepartments store, String department) {
        this.name = name;
        store.registerSubscriber(this, department);  // Registro automático do cliente no departamento de interesse
    }

    @Override
    public void update(String product, String department) {
        System.out.println("Olá " + name + ", o produto " + product + " está em promoção no departamento de " + department + "!");
    }
}
