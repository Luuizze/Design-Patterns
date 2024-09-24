#Antônio Horácio Rodrigues de Magalhães
#Carlos Henrique Racobaldo Luz Montes
#Luiz Guilherme Guerreiro
#Maria Eduarda Lopes de Morais Brito
#Enzo Gebauer

# Definição das classes de ingredientes
class Pao:
    def __init__(self, tipo):
        self.tipo = tipo

class Queijo:
    def __init__(self, tipo):
        self.tipo = tipo

class Presunto:
    def __init__(self, tipo):
        self.tipo = tipo

class Salada:
    def __init__(self, tipo):
        self.tipo = tipo

# Classe Sanduiche
class Sanduiche:
    def __init__(self, pao, queijo, presunto, salada):
        self.pao = pao
        self.queijo = queijo
        self.presunto = presunto
        self.salada = salada

    def __str__(self):
        return (f"Sanduíche com pão {self.pao.tipo}, queijo {self.queijo.tipo}, "
                f"presunto {self.presunto.tipo} e salada {self.salada.tipo}.")

# Classe abstrata Lanchonete (Factory Method)
class Lanchonete:
    def criar_sanduiche(self):
        raise NotImplementedError("Este método deve ser implementado pelas subclasses")

# Fábricas concretas que herdam de Lanchonete
class LanchoneteCG(Lanchonete):
    def criar_sanduiche(self):
        return Sanduiche(Pao("Integral"), Queijo("Prato"), Presunto("De Frango"), Salada("Sem verdura"))

class LanchoneteJP(Lanchonete):
    def criar_sanduiche(self):
        return Sanduiche(Pao("Francês"), Queijo("Mussarela"), Presunto("De Frango"), Salada("Com verdura"))

class LanchoneteRT(Lanchonete):
    def criar_sanduiche(self):
        return Sanduiche(Pao("Bola"), Queijo("Cheddar"), Presunto("De Peru"), Salada("Sem verdura"))

# Função principal
if __name__ == "__main__":
    lanchonete_cg = LanchoneteCG()
    lanchonete_jp = LanchoneteJP()
    lanchonete_rt = LanchoneteRT()

    sanduiche_cg = lanchonete_cg.criar_sanduiche()
    sanduiche_jp = lanchonete_jp.criar_sanduiche()
    sanduiche_rt = lanchonete_rt.criar_sanduiche()

    print("Lanchonete CG:", sanduiche_cg)
    print("Lanchonete JP:", sanduiche_jp)
    print("Lanchonete RT:", sanduiche_rt)
