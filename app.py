#Cálculo do consumo mensal de energia de acordo com 
# o aparelho e tempo médio de uso

#Entrada
aparelho = input("Qual o aparelho utilizado?")
potencia = float(input("Qual a potência do aparelho em Watts(W)?"))
tempo_medio = float(input("Qual o tempo médio de uso diário em horas?"))

#Valor fixo do custo estimado
valor_kWh = 0.90

#Processamento
consumo_energia = (potencia*tempo_medio*30)/1000
custo_mensal = consumo_energia*valor_kWh

#Saída
print("Aparelho utilizado: " + aparelho)
print(f"Consumo estimado: {consumo_energia} kWh/mês")
print(f"Custo estimado: R$ {custo_mensal: .2f} por mês")