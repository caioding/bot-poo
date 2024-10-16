class Veiculo:
    def __init__(self, marca, modelo, ano, valor_diario):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.valor_diario = valor_diario

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, marca):
        self.__marca = marca
    
    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano): 
        self.__ano = ano

    @property
    def valor_diario(self):
        return self.__valor_diario

    @valor_diario.setter
    def valor_diario(self, valor_diario):
        self.__valor_diario = valor_diario
        