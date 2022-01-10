nmr1 = int(input('Digite o primeiro valor para saber o intervalo entre ele e o segundo : '))
nmr2 = int(input('Digite o segundo valor : '))
nmr3 = int(input('Digite a razao entre eles : '))
valor_t = 0

l1 = (list(range(nmr1,nmr2,nmr3)))
print (l1)
for valor in l1:
    valor_t += valor

print(valor_t)