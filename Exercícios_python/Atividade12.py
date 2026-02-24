# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
from statistics import pvariance

pv = int(input('Primeiro Valor: '))
sv = int(input('Segundo Valor: '))
tv = int(input('Terceiro Valor: '))
me = 0
ma = 0

if pv< sv and tv:
    me = pv
if sv< pv and tv:
    me = sv
if tv< pv and sv:
    me = tv
if pv> sv and tv:
    ma = pv
if sv> pv and tv:
    ma = sv
if tv> pv and sv:
    ma = tv

print(f'O menor valor digitado foi {me}')
print(f'O maior valor digitado foi {ma}')