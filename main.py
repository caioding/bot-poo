# main.py

# Importa as classes do pacote 'veiculos_classes'
from veiculos_classes import Veiculo, Carro, Motocicleta

# Criando instâncias
carro1 = Carro(marca="Toyota", modelo="Corolla", ano=2020, valor_diario=150, tipo_combustivel="Gasolina")
moto1 = Motocicleta(marca="Yamaha", modelo="MT-03", ano=2021, valor_diario=100, cilindrada=300)

# Testando as instâncias
print(carro1)
print(moto1)

valor_aluguel_carro = carro1.calcular_valor_aluguel(dias=10, desconto=0.05)
print(f"Valor do aluguel do carro por 10 dias com 5% de desconto: {valor_aluguel_carro}")

valor_aluguel_moto = moto1.calcular_valor_aluguel(dias=5)
print(f"Valor do aluguel da motocicleta por 5 dias: {valor_aluguel_moto}")

# Verificando o total de veículos
total_veiculos = Veiculo.get_total_veiculos()
print(f"Total de veículos: {total_veiculos}")