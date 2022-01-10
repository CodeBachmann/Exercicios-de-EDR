a = 1
b = 1
l1 = []
cont = 0
l2 = []
acum = 0
while cont < 1000:
    l1.append(f'{a}/{b} +')
    cont+=1
    a += 1
    b += 2
    acum += a/b


l1 = ' '.join(l1)
l1 = l1.strip('+')
print(f'S = {l1}\nSoma = {acum:.2f}')