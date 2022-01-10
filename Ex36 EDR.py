tabuda = int(input('Informe qual o numero da tabuada : '))
comeca = int(input('Informe o valor inicial da tabuada : '))
termina = int(input('Informe o valor final da tabuda : '))
while comeca >= termina:
    print('Os valores informados são invalidos : ')
    comeca = int(input('Informe o valor inicial da tabuada : '))
    termina = int(input('Informe o valor final da tabuda : '))

for valor in range(comeca,termina+1):
    print(f'{tabuda} X {valor} = {tabuda*valor}')