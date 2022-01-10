print('Prova')
cont = 0
pontos = 0
lg = input('Digite o gabarito : ').upper()
lg = lg.split(' ')
print(lg)
cont = 0
for valor in lg:
    cont += 1
    resposta = input(f'Digite a reposta da {cont}° questão : ').upper()
    if valor == resposta:
        pontos += 1


print(f'Nota = {pontos}')
