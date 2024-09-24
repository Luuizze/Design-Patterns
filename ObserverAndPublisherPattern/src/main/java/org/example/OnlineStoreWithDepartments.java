package org.example;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class OnlineStoreWithDepartments implements Publisher {
    private Map<String, List<Subscriber>> departmentSubscribers;

    public OnlineStoreWithDepartments() {
        departmentSubscribers = new HashMap<>();
    }

    @Override
    public void registerSubscriber(Subscriber subscriber, String department) {
        departmentSubscribers.putIfAbsent(department, new ArrayList<>());
        departmentSubscribers.get(department).add(subscriber);
    }

    @Override
    public void removeSubscriber(Subscriber subscriber, String department) {
        List<Subscriber> subscribers = departmentSubscribers.get(department);
        if (subscribers != null) {
            subscribers.remove(subscriber);
        }
    }

    @Override
    public void notifySubscribers(String department, String product) {
        List<Subscriber> subscribers = departmentSubscribers.get(department);
        if (subscribers != null) {
            for (Subscriber subscriber : subscribers) {
                subscriber.update(product, department);
            }
        }
    }

    public void setProductOnSale(String department, String product) {
        notifySubscribers(department, product);
    }
}
