altura = 1.00
codigo = 1
maaltura = 0
mnaltura = 0
macdg = 0
mnacdg = 0
mpeso = 0
mpcdg = 0
mnpeso = 0
acump = 0
acuma = 0
cont = 0
lcodigos = []
print('\n\nDigite codigo = 0 para encerrar o programa!!! \n\n')
while codigo != 0:
    while cont == len(lcodigos):
        codigo = int(input('Digite seu codigo : '))
        if codigo != 0:
            if codigo not in lcodigos:
                lcodigos.append(codigo)
            else:
                print('Codigo Repetido!')
            cont+=1
            altura = float(input('Digite sua altura : '))
            acuma += altura
            peso = float(input('Digite seu peso : '))
            acump += peso
            if mnpeso > peso or mnpeso == 0:
                mnpeso = peso
                mnpcdg = codigo
            if mpeso < peso:
                mpeso = peso
                mpcdg = codigo
            if maaltura < altura:
                maaltura = altura
                macdg = codigo
            if mnaltura > altura or mnaltura == 0:
                mnaltura = altura
                mnacdg = codigo
        else:
            cont += 1
cont -= 1
mediap = acump/cont
mediaa = acuma/cont

print(f'O cliente mais alto codigo : {macdg} tem {maaltura:.2f}m')
print(f'O cliente mais pesado codigo : {mpcdg} tem {mpeso:.2f}Kg')
print(f'O cliente mais baixo codigo : {mnacdg} tem {mnaltura:.2f}m')
print(f'O cliente mais magro codigo : {mnpcdg} tem {mnpeso:.2f}Kg')
print(f'A media de altura entre os clientes é {mediaa:.2f}m')
print(f'A media de peso entre os clientes é {mediap:.2f}Kg')
print(f'Codigos registrados{list(lcodigos)}')