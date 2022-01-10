cont = 0
determinante = int(input('Digite a quantidade de idades que você deseja registrar : '))
acum = 0

while cont < determinante:
    idade = int(input('Digite uma idade para registrar : '))
    acum += idade
    cont += 1

media = int(acum/cont)
if media in range(0,26):
    print(f'A media de idade é {media} anos considerada jovem')
elif media in range (26,61):
    print(f'A media de idade é {media} anos considerada adulta')
else:
    print(f'A media de idade é {media} anos considerada idosa')

input('\n\nEnter para finalizar!')