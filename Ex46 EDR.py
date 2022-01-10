acum = 0
cont = 0
nome_atleta = 'a'
melhor_salto = 0
pior_salto = 0
l1 = []
while nome_atleta != '':
    cont = 0
    nome_atleta = (input('Informe o nome do atleta : '))

    if nome_atleta != '':

        while cont < 5:

            cont += 1

            salto = float(input(f'Informe a distancia do seu {cont}° : '))
            l1.append(salto)

            if pior_salto > salto or pior_salto == 0:
                pior_salto = salto

            if melhor_salto < salto:
                melhor_salto = salto

            acum += salto
            print(salto)

        media_salto = (acum-melhor_salto-pior_salto)/(cont-2)
        print(f'Atleta: {nome_atleta}\n'
              f'\nPrimeiro Salto: {l1[0]} m'
              f'\nSegundo Salto: {l1[1]} m'
              f'\nTerceiro Salto: {l1[2]} m'
              f'\nQuarto Salto: {l1[3]} m'
              f'\nQuinto Salto: {l1[4]} m'
              f'\n\nMelhor Salto: {melhor_salto} m'
              f'\nPior Salto: {pior_salto} m'
              f'\nMedia dos demais saltos: {media_salto} m'
              f'\n\nResultado final:'
              f'\n{nome_atleta}: {media_salto} m')