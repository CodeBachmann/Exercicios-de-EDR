cont = 0
nmr = 0
acunmr = 0

while cont < 5:
    nmr = int(input('Digite um numero : '))
    acunmr += nmr
    cont+= 1

print(f'A soma dos numeros digitados é : {acunmr}')
acunmr = acunmr/cont
print(f'A media dos numeros digitados é : {acunmr}')