class Carro(Veiculo):
    def __init__(self, nome, marca, modelo, ano, valor_diario, tipo_combustivel):
        super().__init__(nome, marca, modelo, ano, valor_diario)
        self.__tipo_combustivel = tipo_combustivel

    @property
    def tipo_combustivel(self):
        return self.__tipo_combustivel
    
    @tipo_combustivel.setter
    def tipo_combustivel(self):
        self.__tipo_combustivel

  
    #### Aguardando método de calcular aluguel na class Veiculo