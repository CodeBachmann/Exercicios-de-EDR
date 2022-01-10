
voto = 1
candidato_a = 0
candidato_b = 0
candidato_c = 0
candidato_d = 0
voto_nulo = 0
voto_em_branco = 0
print(f'LISTA DE VOTOS :\n1 - Candidato A\n2 - Candidato B\n3 - Candidato C\n 4 - Candidato D\n5 - Voto Nulo\n6 - Voto em Branco\n0 - Terminar votação')
while voto != 0:
    voto = int(input('Digite seu voto : '))
    if voto !=0:
        if voto == 1:
            candidato_a += 1
        elif voto == 2:
            candidato_b += 1
        elif voto == 3:
            candidato_c += 1
        elif voto == 4:
            candidato_d += 1
        elif voto == 5:
            voto_nulo += 1
        elif voto == 6:
            voto_em_branco += 1

print(f'Candidato A : {candidato_a} votos')
print(f'Candidato B : {candidato_b} votos')
print(f'Candidato C : {candidato_c} votos')
print(f'Candidato D : {candidato_d} votos')
print(f'Votos nulos : {voto_nulo} votos')
print(f'Votos em Branco : {voto_em_branco} votos')

