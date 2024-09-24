package org.example;

import java.util.ArrayList;
import java.util.List;

public class OnlineStore implements Subject {
    private List<Observer> observers;
    private String productOnSale;

    public OnlineStore() {
        observers = new ArrayList<>();
    }

    public void setProductOnSale(String product) {
        this.productOnSale = product;
        notifyObservers();
    }

    @Override
    public void registerObserver(Observer observer) {
        observers.add(observer);
    }

    @Override
    public void removeObserver(Observer observer) {
        observers.remove(observer);
    }

    @Override
    public void notifyObservers() {
        for (Observer observer : observers) {
            observer.update(productOnSale);
        }
    }
}


