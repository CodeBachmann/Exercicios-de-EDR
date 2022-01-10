codigos = []
cont = 0
menor_indice = 0
codigo_menor_indice = 0
maior_indice = 0
codigo_maior_indice = 0
cont_menos_2000 = 0
quantidade_carros = 0
codigo = 0
acum_acidentes_menos_2000 = 0
while cont < 5:
    while cont == len(codigos):
        codigo = int(input('Digite o codigo da cidade : '))
        if codigo not in codigos:
            codigos.append(codigo)
    cont += 1
    quantidade_carros = int(input('Qual a quantidade de carros na sua cidade em 1999 : '))
    numero_acidentes = int(input('Qual o numero de acidentes de carro na sua cidade em 1999 : '))
    if quantidade_carros < 2000:
        acum_acidentes_menos_2000 += numero_acidentes
        cont_menos_2000 += 1
    indice = numero_acidentes/365
    if menor_indice > indice or menor_indice == 0:
        menor_indice = indice
        codigo_menor_indice = codigo
    if maior_indice < indice or maior_indice == 0:
        maior_indice = indice
        codigo_maior_indice = codigo

media_carros = quantidade_carros/cont
media_acidentes_menos_2000 = acum_acidentes_menos_2000/cont_menos_2000

print(f'O maior indice de acidentes {maior_indice:.2f} por dia da cidade {codigo_maior_indice}')
print(f'O menor indice de acidentes {menor_indice:.2f} por dia da cidade {codigo_menor_indice}')
print(f'A media de veiculos das cidades é {media_carros} por cidade')
print(f'A media de acidentes em cidades com menos de 2000 veiculos é {media_acidentes_menos_2000} por ano')

input('DIGITE ENTER PARA ENCERRAR O PROGRAMA!')