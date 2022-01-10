l0 = []
l26 = []
l51 = []
l76 = []
numero = 1
while numero > -1:
    numero = int(input('Digite um numero para saber em qual conjunto ele se encontra : '))
    if numero != 0:
        if numero in range(0,26):
            l0.append(numero)
        elif numero in range(26,51):
            l26.append(numero)
        elif numero in range(51,76):
            l51.append(numero)
        elif numero in range(76,101):
            l76.append(numero)
        else:
            pass

print(f'Foram registrados {len(l0)} numeros entre [0 e 25]')
print(f'Foram registrados {len(l26)} numeros entre [26 e 50]')
print(f'Foram registrados {len(l51)} numeros entre [51 e 75]')
print(f'Foram registrados {len(l76)} numeros entre [76 e 100]')

input('DIGITE ENTER PARA ENCERRAR O PROGRAMA!')