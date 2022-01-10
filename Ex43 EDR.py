print(f'Especificação    Codigo   Preço:')
print(f'Cachorro Quente  100      R$1,20')
print(f'Bauru Simples    101      R$1,30')
print(f'Bauru com ovo    102      R$1,50')
print(f'Hámburguer       103      R$1,20')
print(f'Cheeseburguer    104      R$1,30')
print(f'Refrigerante     105      R$1,00')
print(f'\n\nPARA ENCERRAR DIGITE CODIGO 0!!!')
codigo = 1
acum = 0
while codigo != 0:
    codigo = int(input('Digite o codigo do produto : '))
    if codigo != 0:
        quantidade = int(input('Digite a quantidade do produto : '))
        if codigo == 100 or codigo == 103:
            valor = 1.20
        elif codigo == 101 or codigo == 104:
            valor = 1.30
        elif codigo == 102:
            valor = 1.50
        elif codigo == 105:
            valor = 1
        else:
            print('Codigo invalido')
            valor = 0
        acum += valor*quantidade
print(f'Valor das compras R${acum:.2f}')

input('DIGITE ENTER PARA ENCERRAR O PROGRAMA!')