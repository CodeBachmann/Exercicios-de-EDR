print('Loja Do BACHMANN')
parar = False
cont = 0
acum = 0
cont2 = 0
l1 = []
while parar == False:
    cont += 1
    preco = int(input(f'Informe o valor do {cont}° Produto : '))
    l1.append(preco)
    if preco == 0:
        parar = True
total = 0
for valor in l1:
    total += valor

vcliente = int(input(f'Valor a pagar : R${total:.2f}\nQual o valor que o cliente pagou :'))

troco = vcliente - total

for valor in l1:
    cont2 += 1
    print(f'Produto {cont2}   - R${valor}')
print(f'Valor total : R${total}')
print(f'Valor pago  : R${vcliente}')
print(f'Troco       : R${troco}')

input('\n\nEnter para finalizar!')