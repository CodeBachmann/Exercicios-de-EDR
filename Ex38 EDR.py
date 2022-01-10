salario = int(input('Digite o salario inicial de 1996 : '))
ano = 1996
correcao = 0.0075
while ano < 2021:
    correcao = (2*correcao)
    salariof = salario * (1+correcao)
    ano += 1
    print(salariof)

print(salariof)