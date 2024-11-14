/*
 Equipe:
    Antônio Horácio Rodrigues de Magalhães
    Carlos Henrique Racobaldo Luz Montes
    Luiz Guilherme Guerreiro Carvalho
    Maria Eduarda Lopes de Morais Brito
 */

import java.util.ArrayList;
import java.util.List;

interface Quackable {
   void quack();
}

class MallardDuck implements Quackable {
   @Override
   public void quack() {
       System.out.println("Quack!");
   }
}

class RedheadDuck implements Quackable {
   @Override
   public void quack() {
       System.out.println("Quack!");
   }
}

class DuckCall implements Quackable {
   @Override
   public void quack() {
       System.out.println("Kwak!");
   }
}

class RubberDuck implements Quackable {
   @Override
   public void quack() {
       System.out.println("Squeak!");
   }
}

class QuackCounter implements Quackable {
   
    private Quackable duck;
    private static int quackCount;
    
    public QuackCounter(Quackable duck) {
       this.duck = duck;
   }
   
   @Override
   public void quack() {
       duck.quack();
       quackCount++;
   }

   public static int getQuacks() {
       return quackCount;
   }
}

abstract class AbstractDuckFactory {
   public abstract Quackable createMallardDuck();
   public abstract Quackable createRedheadDuck();
   public abstract Quackable createDuckCall();
   public abstract Quackable createRubberDuck();
}

class CountingDuckFactory extends AbstractDuckFactory {
  
    @Override
    public Quackable createMallardDuck() {
        return new QuackCounter(new MallardDuck());   
    }

   @Override
   public Quackable createRedheadDuck() {
       return new QuackCounter(new RedheadDuck());
   }

   @Override
   public Quackable createDuckCall() {
       return new QuackCounter(new DuckCall());
   }

   @Override
   public Quackable createRubberDuck() {
       return new QuackCounter(new RubberDuck());
   }
}

class Flock implements Quackable {
   
    private List<Quackable> quackers = new ArrayList<>();
    public void add(Quackable quacker) {
           quackers.add(quacker);
   }

   @Override
   public void quack() {
       for (Quackable quacker : quackers) {
           quacker.quack();
       }
   }
}

interface Observer {
   void update(Quackable duck);
}

class Quackologist implements Observer {
  
    @Override
    public void update(Quackable duck) {
       System.out.println("Quackologist: " + duck.getClass().getSimpleName() + " 
just quacked.");
   }
}

class Observable {
   private List<Observer> observers = new ArrayList<>();
   private Quackable duck;
  
   public Observable(Quackable duck) {
       this.duck = duck;
   }
   
   public void registerObserver(Observer observer) {
       observers.add(observer);
   }
   
   public void notifyObservers() {
       for (Observer observer : observers) {
           observer.update(duck);
       }
   }
}

class ObservableQuack implements Quackable {
   
    private Quackable duck;
    private Observable observable;
    public ObservableQuack(Quackable duck) {
       this.duck = duck;
       this.observable = new Observable(this);
   }

   @Override
   public void quack() {
       duck.quack();
       notifyObservers();
   }

   public void registerObserver(Observer observer) {
       observable.registerObserver(observer);
   }

   public void notifyObservers() {
       observable.notifyObservers();
   }
}

public class DuckSimulator {
   
    public static void main(String[] args) {
       DuckSimulator simulator = new DuckSimulator();
       AbstractDuckFactory duckFactory = new CountingDuckFactory();
       simulator.simulate(duckFactory);
   }

   void simulate(AbstractDuckFactory duckFactory) {
       Quackable mallardDuck = duckFactory.createMallardDuck();
       Quackable redheadDuck = duckFactory.createRedheadDuck();
       Quackable duckCall = duckFactory.createDuckCall();
       Quackable rubberDuck = duckFactory.createRubberDuck();
       Flock flockOfDucks = new Flock();
       flockOfDucks.add(mallardDuck);
       flockOfDucks.add(redheadDuck);
       flockOfDucks.add(duckCall);
       flockOfDucks.add(rubberDuck);
       Flock flockOfMallards = new Flock();
       flockOfMallards.add(duckFactory.createMallardDuck());
       flockOfMallards.add(duckFactory.createMallardDuck());
       flockOfMallards.add(duckFactory.createMallardDuck());
       flockOfDucks.add(flockOfMallards);
       System.out.println("Duck Simulator:");
       simulate(flockOfDucks);
       System.out.println("The ducks quacked " + QuackCounter.getQuacks() + " 
times");
   }
   
   void simulate(Quackable duck) {
       duck.quack();
   }
}