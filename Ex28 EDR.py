qnt_cd = int(input('Informe a quantidade de CDs : '))
cont = 0
acum = 0
while qnt_cd > cont:
    cont += 1
    valor_cd = int(input(f'Informe o valor do {cont}° CD : '))
    acum += valor_cd

media = int(acum/cont)

print(f'Foram registrados {cont} CDs com o valor medio de R${media} cada')