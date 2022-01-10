fatorado = int(input('Digite um numero para ser fatorado : '))
cont = 0
b = 1
a = 2
l1 = [1, 2]
while cont < fatorado:
    b = b * a
    a += 1
    cont += 1
    l1.append(a)
print(b)
l1.pop()
l1.pop()
l1.reverse()
print(f'{fatorado} = ',end='')
for valor in l1:
    if valor != 1:
        print(f'{valor} * ',end='')
    else:
        print(f'{valor} = ',end='')

print(b)
input('\n\nEnter para finalizar!')