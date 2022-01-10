cont = 0
nmr = 0
nmr_max = 0
while cont < 5:
    nmr = int(input('Digite um numero : '))
    if nmr > nmr_max:
        nmr_max = nmr

    cont+= 1

print(f'O maior numero digitado foi : {nmr_max}')