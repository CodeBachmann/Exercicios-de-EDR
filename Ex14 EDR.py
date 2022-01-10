
print('BEM VINDO AO DETECTOR DE PARES E IMPARES DO BACHMANN\n\n')
cont = 0
contp = 0
conti = 0

while cont < 10:
    nmr = int(input('Digite um numero inteiro : '))
    if nmr %2 == 0:
        contp += 1
    else:
        contn += 1
    cont+= 1

print(f'Foram registrados {contp} numeros pares e {conti} numeros impares ')