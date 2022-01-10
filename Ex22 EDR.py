nmr2 = int(input('Informe um numero para saber se ele é primo e por quais numeros ele é divisivel: '))
passar = True

if nmr2 != 2 and nmr2%2 == 0:
    pass
elif nmr2 != 3 and nmr2%3 == 0:
    pass
elif nmr2 != 5 and nmr2%5 == 0:
    pass
elif nmr2 != 7 and nmr2%7 == 0:
    pass
elif nmr2 != 11 and nmr2%11 == 0:
    pass
elif nmr2 !=23 and nmr2%23 == 0:
    pass
else:
    print(f'O numero {nmr2} é primo!')
    passar = False
if passar == True:
    if nmr2%2 == 0:
        print(f'{nmr2} é divisivel por 2!')

    if nmr2%3 == 0:
         print(f'{nmr2} é divisivel por 3!')

    if nmr2%5 == 0:
        print(f'{nmr2} é divisivel por 5!')

    if nmr2%7 == 0:
        print(f'{nmr2} é divisivel por 7!')

    if nmr2%11 == 0:
        print(f'{nmr2} é divisivel por 11!')
