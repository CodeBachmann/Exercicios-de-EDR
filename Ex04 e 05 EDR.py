

parar = False
while parar == False:

    pais_a = int(input('Digite a população do pais A : '))
    crescimento_a = float(input('Digite a taxa de crescimento população do pais A : '))
    pais_b = int(input('Digite a população do pais B : '))
    crescimento_b = float(input('Digite a taxa de crescimento população do pais B : '))
    cont = 0

    while pais_a < pais_b:
        pais_a *= crescimento_a
        pais_b *= crescimento_b



        print(f'Pais A : {pais_a:.0f}\nPais B : {pais_b:.0f}')
        cont += 1

    print(f'Foram necessarios {cont} anos para o Pais A alcançar a população do Pais B\n'
          f'A população de A ficou em {pais_a:.0f} e a de B em {pais_b:.0f}')
    continuar = input('Deseja continuar? S para sim e N para não : ').upper()
    if continuar == 'N':
        parar = True