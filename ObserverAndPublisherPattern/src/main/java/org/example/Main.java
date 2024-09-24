package org.example;

import java.util.Scanner;

public class Main {
/*
	@autor: Antônio Horácio Rodrigues de Magalhães;
	        Enzo Gebauer;
            Carlos Henrique Racobaldo Luz Montes;
            Maria Eduarda Lopes de Morais Brito;
            Luiz Guilherme Guerreiro Carvalho;
	@data: 26/08/2024
*/


    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Escolha o padrão que deseja executar:");
        System.out.println("1 - Padrão Observador");
        System.out.println("2 - Padrão Publisher-Subscriber");
        System.out.print("Digite sua escolha (1 ou 2): ");

        int escolha = scanner.nextInt();

        switch (escolha) {
            case 1:
                runObserverPattern();
                break;
            case 2:
                runPublisherSubscriberPattern();
                break;
            default:
                System.out.println("Escolha inválida. Por favor, execute o programa novamente e selecione 1 ou 2.");
        }

        scanner.close();
    }

    // Parte 1: Padrão Observador
    public static void runObserverPattern() {
        System.out.println("\n=== Parte 1: Padrão Observador ===");
        OnlineStore store = new OnlineStore();

        Customer customer1 = new Customer("LG", store);
        Customer customer2 = new Customer("Zoca", store);

        store.setProductOnSale("TV 4K");
        store.setProductOnSale("Acer Laptop 3060");
    }

    // Parte 2: Padrão Publisher-Subscriber
    public static void runPublisherSubscriberPattern() {
        System.out.println("\n=== Parte 2: Padrão Publisher-Subscriber ===");
        OnlineStoreWithDepartments storeWithDepartments = new OnlineStoreWithDepartments();

        CustomerWithDepartmentPreference customerWithDept1 = new CustomerWithDepartmentPreference("LG", storeWithDepartments, "Eletrônicos");
        CustomerWithDepartmentPreference customerWithDept2 = new CustomerWithDepartmentPreference("Zoca", storeWithDepartments, "Roupas");

        storeWithDepartments.setProductOnSale("Eletrônicos", "TV 4K");
        storeWithDepartments.setProductOnSale("Roupas", "Casaco");
    }
}
