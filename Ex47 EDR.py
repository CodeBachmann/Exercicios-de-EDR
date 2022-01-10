l1 = []
acum = 0
menor_nota = 0
maior_nota = 0
cont = 0
nome_atleta = 'a'

while nome_atleta != '':
    nome_atleta = input('Digite o nome do atleta : ')
    if nome_atleta != '':
        while cont < 10:
            cont += 1
            nota = float(input(f'Digite a sua {cont}° nota '))
            l1.append(nota)
            if menor_nota > nota or menor_nota == 0:
                menor_nota = nota
            if maior_nota < nota:
                maior_nota = nota
            acum += nota
    media_nota = (acum-menor_nota-maior_nota)/(cont-2)
    print(f'Atleta: {nome_atleta}')
    for valor in l1:
        print(f'Nota: {valor:.1f}')

    print(f'\nResultado final:'
          f'\nAtleta: {nome_atleta}'
          f'Melhor nota: {maior_nota:.1f}'
          f'Pior nota: {menor_nota:.1f}'
          f'Media: {media_nota:.1f}')