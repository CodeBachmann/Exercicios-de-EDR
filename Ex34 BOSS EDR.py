primo = int(input('Digite um numero para saber se ele é primo : '))
divisor = float(primo) ** 0.5
divisor = int(divisor)
if divisor%2 == 0:
    divisor+= 1
if primo%2 == 0:
    print(f'{primo} não é primo!')
    exit()
while divisor != 1:

    if primo%divisor == 0:
        print(f'{primo} não é primo!')
        exit()
    divisor -= 2
    if divisor == 1:
        print(f'{primo} é primo!')

input('Enter para finalizar!!')

