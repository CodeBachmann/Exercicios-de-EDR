print('BEM VINDO AO MEDIDOR DE TEMPERATURA DO BACHMANN!!!\n\n')
print('Digite 0 para concluir a adição de dados \n\n')
maior = 0
menor = 0
cont = 0
parar = False
while parar == False:
    temperatura = int(input('\nAdicione uma temperatura em C° : '))
    if temperatura != 0:
        if maior == 0:
            maior = temperatura
        elif maior < temperatura:
            maior = temperatura
        if menor == 0:
            menor = temperatura
        elif menor > temperatura:
            menor = temperatura
    else:
        parar = True
print(f'\n\nMaior temperatura : {maior}C°\nMenor temperatura : {menor}C°')
input('\n\nENTER PARA FINALIZAR!')