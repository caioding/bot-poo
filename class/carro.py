class Carro(Veiculo):
    def __init__(self, nome, marca, modelo, ano, valor_diario, tipo_combustivel):
        super().__init__(nome, marca, modelo, ano, valor_diario)
        self.tipo_combustivel = tipo_combustivel