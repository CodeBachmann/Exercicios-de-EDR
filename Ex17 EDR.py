import time

print('BEM VINDO AO FATORADOR GENTE BOA DO BACHMANN!!!\n\n')

fatorial = int(input('Digite um valor para ser fatorado : '))
cont = 0
a = 1
b = 1
c = a * b
while cont < fatorial:

    a = a * b
    b += 1
    cont += 1

print(a)
