print('BEM VINDO AO VERIFICADOR DE PRIMOS DO BACHMANN!!!\n\n')

parar = False
poppar = True
while parar == False:
    primos = [2,3,5,7,11]
    determinante = int(input('\n\nQual numero você deseja saber se é primo : '))

    for numero in range(23,int(determinante/2)+1,2):
        nmr = numero
        primo = True
        if nmr not in primos:
            for valor in primos:
                if valor * 2 < nmr:
                    if nmr%valor == 0 and nmr != valor :
                        primo = False

                else:
                    for valor in primos:
                        if determinante%valor == 0:
                            poppar = False

                        else:
                            if determinante not in primos:
                               primos.append(determinante)

        if poppar == False and determinante in primos:
            primos.pop()
        if primo == True:
            primos.append(nmr)
            print(f'{nmr}/{determinante/2}')
        if determinante in primos:
            break

    if determinante in primos:
        print(f'{determinante} é primo!')
    else:
        print(f'{determinante} não é primo!')
    print(list(primos))



    input('\n\nENTER PARA FINALIZAR!')