
menor_num = 0

maior_num = 0

acum = 0

determinante = int(input('Quantos numeros você deseja adicionar : '))

cont = 0

while cont < determinante:
    valor = int(input('Adicione um valor :'))
    if valor in range(1001):

        if maior_num < valor:
            maior_num = valor

        if menor_num == 0:
            menor_num = valor

        if menor_num > valor:
            menor_num = valor

        acum += valor
        cont+= 1

    else:
        print('Valor digitado fora do parametro [0 a 1000]')

print(f'O maior valor registrado foi {maior_num} e o menor foi {menor_num}'
      f'\nA soma dos valores é {acum}')