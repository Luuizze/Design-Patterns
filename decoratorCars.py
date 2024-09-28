# EQUIPE
# Antônio Horácio Rodrigues de Magalhães
# Carlos Henrique Racobaldo Luz Montes
# Luiz Guilherme Guerreiro Carvalho
# Maria Eduarda Lopes de Morais Brito
# Enzo Gebauer


# Classe base para carros
class Carro:
    def get_descricao(self):
        return "Carro básico"

    def get_custo(self):
        return 0.0


# Tipos de carros específicos
class Hatch(Carro):
    def get_descricao(self):
        return "Hatch"

    def get_custo(self):
        return 20000.0


class Sedan(Carro):
    def get_descricao(self):
        return "Sedan"

    def get_custo(self):
        return 25000.0


class SUV(Carro):
    def get_descricao(self):
        return "SUV"

    def get_custo(self):
        return 30000.0


# Decorador base para adicionar recursos
class CarroDecorator(Carro):
    def __init__(self, carro):
        self._carro = carro

    def get_descricao(self):
        return self._carro.get_descricao()

    def get_custo(self):
        return self._carro.get_custo()


# Decoradores específicos
class FreiosABS(CarroDecorator):
    def get_descricao(self):
        return f"{self._carro.get_descricao()} com freios ABS"

    def get_custo(self):
        return self._carro.get_custo() + 1500.0


class MotorTurbo(CarroDecorator):
    def get_descricao(self):
        return f"{self._carro.get_descricao()} com motor turbo"

    def get_custo(self):
        return self._carro.get_custo() + 5000.0


class SuspensaoEletronica(CarroDecorator):
    def get_descricao(self):
        return f"{self._carro.get_descricao()} com suspensão eletrônica"

    def get_custo(self):
        return self._carro.get_custo() + 2500.0


# Testando a solução
if __name__ == "__main__":
    # Criando um carro básico
    carro = Hatch()
    print(carro.get_descricao(), "- Custo:", carro.get_custo())

    # Adicionando freios ABS
    carro_com_abs = FreiosABS(carro)
    print(carro_com_abs.get_descricao(), "- Custo:", carro_com_abs.get_custo())

    # Adicionando motor turbo ao carro com freios ABS
    carro_com_abs_turbo = MotorTurbo(carro_com_abs)
    print(carro_com_abs_turbo.get_descricao(), "- Custo:", carro_com_abs_turbo.get_custo())

    # Adicionando suspensão eletrônica ao carro com freios ABS e motor turbo
    carro_completo = SuspensaoEletronica(carro_com_abs_turbo)
    print(carro_completo.get_descricao(), "- Custo:", carro_completo.get_custo())
