# Antônio Horácio Rodrigues de Magalhães
# Carlos Henrique Racobaldo Luz Montes
# Maria Eduarda Lopes de Morais Brito
# Luiz Guilherme Guerrero
# Enzo Gebauer

from abc import ABC, abstractmethod

# Classe abstrata para as bebidas
class Beverage(ABC):
    SMALL = "alto"
    MEDIUM = "grande"
    LARGE = "venti"
    
    def __init__(self):
        self.size = Beverage.SMALL
    
    @abstractmethod
    def cost(self):
        pass

    def setSize(self, size):
        self.size = size

    def getSize(self):
        return self.size

# Classe concreta para uma bebida específica (Café Espresso)
class Espresso(Beverage):
    def cost(self):
        return 1.99

    def __str__(self):
        return "Espresso"

# Outra bebida concreta (Café Dark Roast)
class DarkRoast(Beverage):
    def cost(self):
        return 2.49

    def __str__(self):
        return "Dark Roast"

# Classe abstrata para os condimentos (Decorator)
class CondimentDecorator(Beverage, ABC):
    def __init__(self, beverage):
        self.beverage = beverage

    def getSize(self):
        return self.beverage.getSize()

# Condimento específico: Mocha
class Mocha(CondimentDecorator):
    def cost(self):
        size = self.getSize()
        extra_cost = 0.10 if size == Beverage.SMALL else 0.15 if size == Beverage.MEDIUM else 0.20
        return self.beverage.cost() + extra_cost

    def __str__(self):
        return str(self.beverage) + ", Mocha"

# Condimento específico: Whip (creme)
class Whip(CondimentDecorator):
    def cost(self):
        size = self.getSize()
        extra_cost = 0.10 if size == Beverage.SMALL else 0.15 if size == Beverage.MEDIUM else 0.20
        return self.beverage.cost() + extra_cost

    def __str__(self):
        return str(self.beverage) + ", Whip"

# Outra bebida concreta: House Blend
class HouseBlend(Beverage):
    def cost(self):
        return 1.89

    def __str__(self):
        return "House Blend"

# Exemplo de uso
if __name__ == "__main__":
    # Pedido 1: Espresso sem condimentos, tamanho grande
    beverage1 = Espresso()
    beverage1.setSize(Beverage.MEDIUM)
    print(f"Bebida: {beverage1}, Custo: ${beverage1.cost():.2f}")

    # Pedido 2: Dark Roast com 2 Mocha e 1 Whip, tamanho venti
    beverage2 = DarkRoast()
    beverage2.setSize(Beverage.LARGE)
    beverage2 = Mocha(beverage2)
    beverage2 = Mocha(beverage2)
    beverage2 = Whip(beverage2)
    print(f"Bebida: {beverage2}, Custo: ${beverage2.cost():.2f}")

    # Pedido 3: House Blend com Mocha, Soy, Whip, tamanho alto
    beverage3 = HouseBlend()
    beverage3.setSize(Beverage.SMALL)
    beverage3 = Mocha(beverage3)
    beverage3 = Whip(beverage3)
    print(f"Bebida: {beverage3}, Custo: ${beverage3.cost():.2f}")