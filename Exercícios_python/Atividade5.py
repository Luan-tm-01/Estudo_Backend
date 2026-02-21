# Faça um programa que leia uma frase pelo teclado e mostra:
# Quantas vezes aparece a letra "A"
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece a última vez

f = str(input('Digite uma Frase: ')).upper().strip()
cf = f.count('A')
p1 = f.find('A')+1
p2 = f.rfind('A')+1

print(f'A letra "A" apareceu {cf} vezes')
print(f'Primeiro apareceu na {p1} posição')
print(f'Por último apareceu na {p2} posição')
