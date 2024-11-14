'''
 Equipe:
    Antônio Horácio Rodrigues de Magalhães
    Carlos Henrique Racobaldo Luz Montes
    Enzo Bacelar Conte Gebauer
    Luiz Guilherme Guerreiro Carvalho
    Maria Eduarda Lopes de Morais Brito
'''

from abc import ABC, abstractmethod

class Iterator(ABC):
    @abstractmethod
    def has_next(self):
        pass
    @abstractmethod
    def next(self):
        pass

class MenuCafeSaborSupremo:
    def __init__(self):
        self.itens = []
        self.adicionar_item("Café Expresso")
        self.adicionar_item("Bolo de Cenoura")
        self.adicionar_item("Croissant")
    def adicionar_item(self, item):
        self.itens.append(item)
    def criar_iterator(self):
        return MenuCafeSaborSupremoIterator(self.itens)

class MenuCafeSaborSupremoIterator(Iterator):
    def __init__(self, itens):
        self.itens = itens
        self.posicao = 0
    def has_next(self):
        return self.posicao < len(self.itens)
    def next(self):
        if self.has_next():
            item = self.itens[self.posicao]
            self.posicao += 1
            return item
        return None
 
class MenuMassasChefGourmet:
    def __init__(self):
        self.itens = [None] * 3
        self.posicao = 0
        self.adicionar_item("Lasanha")
        self.adicionar_item("Ravioli")
        self.adicionar_item("Fettuccine Alfredo")
    def adicionar_item(self, item):
        if self.posicao >= len(self.itens):
            print("O menu está cheio, não é possível adicionar mais itens.")
        else:
            self.itens[self.posicao] = item
            self.posicao += 1
    def criar_iterator(self):
        return MenuMassasChefGourmetIterator(self.itens)

class MenuMassasChefGourmetIterator(Iterator):
    def __init__(self, itens):
        self.itens = itens
        self.posicao = 0
    def has_next(self):
        return self.posicao < len(self.itens) and self.itens[self.posicao] is not None
    def next(self):
        if self.has_next():
            item = self.itens[self.posicao]
            self.posicao += 1
            return item
        return None

class MenuBandejaDeOuro:
    def __init__(self):
        self.itens = {}
        self.adicionar_item(1, "Frango Grelhado")
        self.adicionar_item(2, "Peixe ao Molho")
        self.adicionar_item(3, "Carne Assada")
    def adicionar_item(self, chave, item):
        self.itens[chave] = item
    def criar_iterator(self):
        return MenuBandejaDeOuroIterator(self.itens)

class MenuBandejaDeOuroIterator(Iterator):
    def __init__(self, itens):
        self.elementos = iter(itens.values())
    def has_next(self):
        try:
            self.atual = next(self.elementos)
            return True
        except StopIteration:
            return False
    def next(self):
        if hasattr(self, 'atual'):
            return self.atual
        return None

class Garcom:
    def __init__(self, menu1, menu2, menu3):
        self.menu1 = menu1
        self.menu2 = menu2
        self.menu3 = menu3
    def exibir_cardapios(self):
        iterator_menu1 = self.menu1.criar_iterator()
        iterator_menu2 = self.menu2.criar_iterator()
        iterator_menu3 = self.menu3.criar_iterator()
        print("Cardápio Café Sabor Supremo:")
        self.exibir_menu(iterator_menu1)
        print("\nCardápio Massas do Chef Gourmet:")
        self.exibir_menu(iterator_menu2)
        print("\nCardápio Bandeja de Ouro:")
        self.exibir_menu(iterator_menu3)
    def exibir_menu(self, iterator):
        while iterator.has_next():
            item = iterator.next()
            print(f"- {item}")

if __name__ == "__main__":
    menu_cafe = MenuCafeSaborSupremo()
    menu_massas = MenuMassasChefGourmet()
    menu_bandeja = MenuBandejaDeOuro()
    garcom = Garcom(menu_cafe, menu_massas, menu_bandeja)
    garcom.exibir_cardapios()