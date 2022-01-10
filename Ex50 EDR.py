a=1
b=1
cont = 0
acum =0
contador = int(input('Digite quantos termos você deseja calcular : '))

while cont < contador:
    acum += a/b
    b+=1
    cont+=1

print(f'{acum:.1f}')