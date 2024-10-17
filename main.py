# main.py

# Importa as classes do pacote 'veiculos_classes'
from veiculos_classes import Veiculo, Carro, Motocicleta

# Criando instâncias
carro1 = Carro(marca="Toyota", modelo="Corolla", ano=2020, valor_diario=150, tipo_combustivel="Gasolina")
moto1 = Motocicleta(marca="Yamaha", modelo="MT-03", ano=2021, valor_diario=100, cilindrada=100)

# Testando as instâncias
print(carro1)
print(moto1)

# Aplica aumento de 10% para todos os carros
carro1.aplicar_aumento(10)
moto1.aplicar_aumento(10)

valor_aluguel_carro = carro1.calcular_valor_aluguel(dias=7, desconto=0)
print(valor_aluguel_carro)

valor_aluguel_moto = moto1.calcular_valor_aluguel(dias=5, desconto=0)
print(valor_aluguel_moto)

# Verificando o total de veículos
total_veiculos = Veiculo.get_total_veiculos()
print(f"Total de veículos: {total_veiculos}")
