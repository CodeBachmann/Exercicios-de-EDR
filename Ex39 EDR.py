cdgmalt = 0
malt = 0
mnalt = 0
cdgmnalt = 0
codigo = 1
codigos = []
cont = 0
print(f'Para encerrar o programa digite "0 0"')
while codigo != 0:
    while len(codigos) == cont:
        aec = (input('Informe seu codigo e sua altura : '))
        l2 = []
        l2 = aec.split(' ')
        codigo = int(l2[0])
        altura = int(l2[1])
        if codigo not in codigos:
            codigos.append(codigo)
    if codigo != 0:
        cont += 1
        if mnalt > altura or mnalt == 0:
            mnalt = altura
            cdgmnalt = codigo
        if malt < altura or altura == 0:
            malt = altura
            cdgmalt = codigo

print(f'O aluno mais alto foi o : {cdgmalt} medindo : {malt}cm')
print(f'O aluno mais baixo foi o : {cdgmnalt} medindo : {mnalt}cm')

input('DIGITE ENTER PARA ENCERRAR O PROGRAMA!')


