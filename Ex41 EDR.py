divida = int(input('Digite o valor inicial da sua divida : '))
lista_juros = ['1 ','3 ' ,'6 ' ,'9 ' ,'12',0.0,0.01,0.015,0.02,0.025]
cont = 0

for valor in lista_juros:
    cont+= 1
    juros = divida * lista_juros[4+cont]
    if juros == 0.0:
        valor_divida = divida
    else:
        juros = divida *(juros/100)
        valor_divida = divida + juros
    if valor != '12':
        valor.split(' ')
        divide_parcela = int(valor)
    else:
        divide_parcela = int(valor)

    valor_parcela = valor_divida/divide_parcela
    if juros == 0.0:
        print('Valor da Divida  Valor dos Juros Quantidade de Parcelas Valor da Parcela\n\n')
    if juros == 0:
        print(f'R$ {valor_divida:.0f}               {juros}               {divide_parcela}                 {valor_parcela:.2f}')
    elif divide_parcela == 12:
        print(f'R$ {valor_divida:.0f}             {juros}               {divide_parcela}                {valor_parcela:.2f}')
    else:
        print(f'R$ {valor_divida:.0f}             {juros}               {divide_parcela}                 {valor_parcela:.2f}')


    if cont == 5:
        break

input('DIGITE ENTER PARA ENCERRAR O PROGRAMA!')