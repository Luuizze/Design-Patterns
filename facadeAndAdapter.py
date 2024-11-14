'''
Equipe:
    Antônio Horácio Rodrigues de Magalhães
    Carlos Henrique Racobaldo Luz Montes
    Luiz Guilherme Guerreiro Carvalho
    Maria Eduarda Lopes de Morais Brito
'''

# TransportadoraA
class TransportadoraA:
    def calcular_frete(self, peso, dimensoes, endereco_destino):
        return 50.0  # Valor fixo
    
    def gerar_etiqueta(self, pedido_id):
        return f"Etiqueta-A-{pedido_id}"
    
    def acompanhar_status(self, codigo_rastreamento):
        return "Em trânsito - Transportadora A"

# TransportadoraB
class TransportadoraB:
    def calcular_frete(self, kg, largura, altura, profundidade, destino):
        return 45.0  # Valor fixo
    
    def criar_etiqueta(self, id_pedido):
        return f"Etiqueta-B-{id_pedido}"
    
    def rastrear_pedido(self, rastreamento):
        return "Entregue - Transportadora B"

# TransportadoraC
class TransportadoraC:
    def consultar_frete(self, dados_pedido):
        return {"valor": 40.0}
    
    def emitir_etiqueta(self, pedido):
        return {"etiqueta": f"Etiqueta-C-{pedido}"}
    
    def verificar_status(self, codigo):
        return {"status": "Em processamento - Transportadora C"}

# Interface comum
class TransportadoraInterface:
    def calcularFrete(self, peso, dimensoes, enderecoDestino):
        pass

    def gerarEtiqueta(self, pedidoId):
        pass

    def acompanharPedido(self, codigoRastreamento):
        pass

# Adapter para TransportadoraA
class TransportadoraAAdapter(TransportadoraInterface):
    def __init__(self):
        self.transportadora = TransportadoraA()

    def calcularFrete(self, peso, dimensoes, enderecoDestino):
        return self.transportadora.calcular_frete(peso, dimensoes, enderecoDestino)

    def gerarEtiqueta(self, pedidoId):
        return self.transportadora.gerar_etiqueta(pedidoId)

    def acompanharPedido(self, codigoRastreamento):
        return self.transportadora.acompanhar_status(codigoRastreamento)

# Adapter para TransportadoraB
class TransportadoraBAdapter(TransportadoraInterface):
    def __init__(self):
        self.transportadora = TransportadoraB()

    def calcularFrete(self, peso, dimensoes, enderecoDestino):
        largura, altura, profundidade = dimensoes
        return self.transportadora.calcular_frete(peso, largura, altura, profundidade, enderecoDestino)

    def gerarEtiqueta(self, pedidoId):
        return self.transportadora.criar_etiqueta(pedidoId)

    def acompanharPedido(self, codigoRastreamento):
        return self.transportadora.rastrear_pedido(codigoRastreamento)

# Adapter para TransportadoraC
class TransportadoraCAdapter(TransportadoraInterface):
    def __init__(self):
        self.transportadora = TransportadoraC()

    def calcularFrete(self, peso, dimensoes, enderecoDestino):
        dados = {"peso": peso, "dimensoes": dimensoes, "destino": enderecoDestino}
        return self.transportadora.consultar_frete(dados)["valor"]

    def gerarEtiqueta(self, pedidoId):
        return self.transportadora.emitir_etiqueta(pedidoId)["etiqueta"]

    def acompanharPedido(self, codigoRastreamento):
        return self.transportadora.verificar_status(codigoRastreamento)["status"]

class SistemaDePedidosFacade:
    def __init__(self):
        self.transportadoras = [
            TransportadoraAAdapter(),
            TransportadoraBAdapter(),
            TransportadoraCAdapter()
        ]

    def calcularFrete(self, peso, dimensoes, enderecoDestino):
        # Seleciona a transportadora com menor custo
        custos = [(t, t.calcularFrete(peso, dimensoes, enderecoDestino)) for t in self.transportadoras]
        melhor_opcao = min(custos, key=lambda x: x[1])
        return melhor_opcao

    def gerarEtiqueta(self, transportadora, pedidoId):
        return transportadora.gerarEtiqueta(pedidoId)

    def acompanharPedido(self, transportadora, codigoRastreamento):
        return transportadora.acompanharPedido(codigoRastreamento)

if __name__ == "__main__":
    sistema = SistemaDePedidosFacade()

    # Calcular o frete
    peso = 10
    dimensoes = (20, 30, 40)
    endereco = "Rua Exemplo, 123"
    melhor_transportadora, custo = sistema.calcularFrete(peso, dimensoes, endereco)
    print(f"Melhor transportadora: {melhor_transportadora.__class__.__name__}, Custo: {custo}")

    # Gerar etiqueta
    etiqueta = sistema.gerarEtiqueta(melhor_transportadora, "Pedido123")
    print(f"Etiqueta: {etiqueta}")

    # Acompanhar pedido
    status = sistema.acompanharPedido(melhor_transportadora, "ABC123")
    print(f"Status: {status}")
