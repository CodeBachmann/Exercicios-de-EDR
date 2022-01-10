nmr = -1
while nmr not in range(0,11):
    nmr = int(input('Digite um numero entre 0 e 10 : '))

    if nmr not in range(0,11):
        print('Numero Invalido !!!')
    else:
        print('Numero aceito!')