from .veiculo import Veiculo
class Motocicleta(Veiculo):
    lista_de_veiculos = []

    def __init__(self, marca, modelo, ano, valor_diario, cilindrada):
        super().__init__(marca, modelo, ano, valor_diario)
        self.__cilindrada = cilindrada
        Motocicleta.lista_de_veiculos.append(self)

    @property
    def cilindrada(self):
        return self.__cilindrada

    @cilindrada.setter
    def cilindrada(self, cilindrada):
        self.__cilindrada = cilindrada

    def calcular_valor_aluguel(self, dias, desconto=0):
        total = super().calcular_valor_aluguel(dias, desconto)
        if self.__cilindrada > 200:
            total += total * 0.1
            return f"Valor do aluguel do carro por {dias:.0f} dias com moto acima de 200cc: R${total:.2f}"
        else:
            return f"Valor do aluguel do carro por {dias:.0f} dias: R${total:.2f}"

    def aplicar_aumento(cls, percentual):
        for veiculo in cls.lista_de_veiculos:
            novo_valor = veiculo._Veiculo__valor_diario + (veiculo._Veiculo__valor_diario * percentual / 100)
            veiculo._Veiculo__valor_diario = novo_valor
