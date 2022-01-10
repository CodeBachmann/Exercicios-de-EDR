
print('BEM VINDO A CALCULADORA EXPONENCIAL DO BACHMANN!!!\n\n')

valor = float(input('Digite um valor base : '))
expoente = float(input('Digite o expoente : '))
cont = 0
valor_t = 1.0
while cont < expoente:
    valor_t *= valor
    cont += 1
    print(valor_t)

print(valor_t)