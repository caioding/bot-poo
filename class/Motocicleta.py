from .veiculo import Veiculo
class Motocicleta(Veiculo):
    def __init__(self, marca, modelo, ano, valor_diario, cilindrada):
        super().__init__(marca, modelo, ano, valor_diario)  # Chama o construtor da classe mãe
        self.__cilindrada = cilindrada

    @property
    def cilindrada(self):
        return self.__cilindrada

    @cilindrada.setter
    def cilindrada(self, cilindrada):
        self.__cilindrada = cilindrada

    # Sobrescrever o método calcular_aluguel
    def calcular_aluguel(self, dias, desconto=None):
        total = super().calcular_aluguel(dias, desconto)  # Chama o método da classe mãe
        if self.__cilindrada > 200:  # Se a cilindrada for maior que 200cc, aplica o custo extra
            total += total * 0.1  # Aumenta o custo em 10%
        return total
