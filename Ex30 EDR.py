cont = 0
preçoi = 0.18
acum = 0

while cont < 50:
    cont+= 1
    acum += preçoi
    print(f'{cont} - R${acum:.2f}')

input('\n\nEnter para finalizar!')