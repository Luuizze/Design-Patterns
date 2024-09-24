package org.example;

public interface Publisher {
    void registerSubscriber(Subscriber subscriber, String department);
    void removeSubscriber(Subscriber subscriber, String department);
    void notifySubscribers(String department, String product);
}

