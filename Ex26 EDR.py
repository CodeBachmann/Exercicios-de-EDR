parar = False
voto_a = 0
voto_b = 0
voto_c = 0
while parar == False:
    print('Digita a letra do candidato para adicionar um voto a ele : ')
    print('Candidato A')
    print('Candidato B')
    print('Candidato C')
    voto = input('Qual seu voto : ').upper()

    if voto == 'A':
        voto_a += 1
    elif voto == 'B':
        voto_b += 1
    elif voto == 'C':
        voto_c += 1

    continuar = input('Deseja continuar votando S para sim e N para não : ').upper()
    if continuar == 'N':
        parar = True
print(f'Votos do candidato A : {voto_a}\nVotos do candidato B : {voto_b}\nVotos do candidato C : {voto_c}')

input('\n\nEnter para finalizar!')
