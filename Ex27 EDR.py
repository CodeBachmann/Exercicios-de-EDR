turma = int(input('Quantas turmas você quer registrar : '))
cont = 0
acum = 0

while cont < turma:
    cont += 1
    alunos = int(input(f'Quantos alunos tem na {cont}° turma : '))

    if alunos > 40:
        cont -= 1
        print('A turma pode ter no maximo 40 alunos!!')
    else:
        acum += alunos

media = int(acum/cont)
print(f'A media de alunos entre as turmas é {media} alunos por turma')

input('\n\nEnter para finalizar!')