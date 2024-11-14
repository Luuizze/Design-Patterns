/*
	@autor: Antônio Horácio Rodrigues de Magalhães;
            Carlos Henrique Racobaldo Luz Montes;
            Maria Eduarda Lopes Brito;
            Luiz Guilherme Guerreiro Carvalho;
	@data: 26/08/2024
*/


#include <iostream>
#include <memory>
#include <string>

// Interface Strategy
class DescontoStrategy {
public:
    virtual double calcularDesconto(double valor) = 0;
    virtual ~DescontoStrategy() = default;
};

// Implementações das estratégias de desconto
class DescontoNatal : public DescontoStrategy {
public:
    double calcularDesconto(double valor) override {
        return valor * 0.25; // 25% de desconto
    }
};

class DescontoAnoNovo : public DescontoStrategy {
public:
    double calcularDesconto(double valor) override {
        return valor * 0.30; // 30% de desconto
    }
};

// Singleton para a fábrica de estratégias de desconto
class DescontoFactory {
private:
    static std::unique_ptr<DescontoFactory> instance;
    DescontoFactory() = default;

public:
    static DescontoFactory* getInstance() {
        if (!instance) {
            instance = std::make_unique<DescontoFactory>();
        }
        return instance.get();
    }

    std::unique_ptr<DescontoStrategy> criarDesconto(const std::string& tipo) {
        if (tipo == "Natal") {
            return std::make_unique<DescontoNatal>();
        } else if (tipo == "AnoNovo") {
            return std::make_unique<DescontoAnoNovo>();
        } else {
            return nullptr;
        }
    }
};

// Inicializando a instância única da fábrica
std::unique_ptr<DescontoFactory> DescontoFactory::instance = nullptr;

// Classe de Venda que utiliza uma estratégia de desconto
class Venda {
private:
    std::unique_ptr<DescontoStrategy> desconto;

public:
    Venda(std::unique_ptr<DescontoStrategy> desconto)
        : desconto(std::move(desconto)) {}

    double aplicarDesconto(double valor) {
        return desconto->calcularDesconto(valor);
    }
};

// Exemplo de uso
int main() {
    auto factory = DescontoFactory::getInstance();

    // Criando uma venda com desconto de Natal
    auto descontoNatal = factory->criarDesconto("Natal");
    Venda vendaNatal(std::move(descontoNatal));
    std::cout << "Desconto de Natal: " << vendaNatal.aplicarDesconto(1000) << std::endl;

    // Criando uma venda com desconto de Ano Novo
    auto descontoAnoNovo = factory->criarDesconto("AnoNovo");
    Venda vendaAnoNovo(std::move(descontoAnoNovo));
    std::cout << "Desconto de Ano Novo: " << vendaAnoNovo.aplicarDesconto(1000) << std::endl;

    return 0;
}
