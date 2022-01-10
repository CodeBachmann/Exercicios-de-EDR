cont = 0
preçoi = 1.99
acum = 0

while cont < 50:
    cont+= 1
    acum += preçoi
    print(f'{cont} - R${acum:.2f}')