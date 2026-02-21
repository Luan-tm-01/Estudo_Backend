#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

c = (str(input('Em qual Cidade você nasceu? ')).upper()).strip()

print(c[:5] == 'SANTO')