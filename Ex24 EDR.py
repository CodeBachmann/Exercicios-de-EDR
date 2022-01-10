determinante = int(input('Digite quantas notas você deseja digitar : '))
cont = 0
acum = 0
while cont < determinante:
    cont += 1
    nota = int(input('Digite uma nota : '))
    acum += nota

media = acum/cont
print(f'A sua media é : {media}')

input('\n\nEnter para finalizar!')