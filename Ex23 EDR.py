print('BEM VINDO AO MEDIDOR DE TEMPERATURA DO BACHMANN!!!\n\n')

determinante = int(input('Qual numero você deseja saber se é primo : '))
parar = False
while parar == False:
    primos = [2,3,5,7,11,13]

    if determinante < 13:
        if determinante in primos:
            print(f'{determinante} é primo')
            exit()
        else:
            print(f'{determinante} não é primo')
            exit()
    for numero in range(13, determinante + 1,2):
        nmr = numero
        primo = True
        if nmr not in primos:
            for valor in primos:
                if nmr%valor == 0 and nmr != valor :
                    primo = False

        if primo == True:
            primos.append(nmr)
            print(f'{nmr} é primo')

    print(list(primos))

    input('\n\nENTER PARA FINALIZAR!')