# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

print('=' * 25)
print('   10 TERMOS DE UMA PA   ')
print('=' * 25)

t = int(input('Primeiro termo: '))
r = int(input('Razão: '))
for i in range (t,10*r,r):
    print(i, end=' -> ')
print(end='ACABOU')