print('BEM VINDO AO FATORADOR CHATINHO DO BACHMANN!!!\n\n')
parar = False
print('O valor a ser fatorado deve ser menor ou igual a 16 Positivo e Inteiro!!!\n\n')
while parar == False:
    fatorial = int(input('Digite um valor para ser fatorado : '))
    cont = 0
    a = 1
    b = 1
    c = a * b
    if fatorial < 16 and fatorial > 0:
        while cont < fatorial:

            a = a * b
            b += 1
            cont += 1

        print(a)

        continuar = input('Você deseja continuar digite S para sim ou N para não : ').upper()
        if continuar == 'N':
            parar = True

input('\n\nEnter para finalizar!')