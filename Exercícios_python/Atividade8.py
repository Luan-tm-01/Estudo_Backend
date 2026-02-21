# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

v = int(input("Qual é a velocidade atual do carro? "))
m = 0
if v <= 80:
    print("Tenha um bom dia! Dirija com segurança!")
else:
    m = float((v-80)*7)
    print(f'MULTADO! Você excedeu o limite permitido que é 80Km/h')
    print(f'Você deve pagar uma multa de R${m:.2f}')
    print("Tenha um bom dia! Dirija com segurança!")