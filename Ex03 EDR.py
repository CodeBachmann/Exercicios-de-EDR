

nome = 'a'
idade = -1
sexo = 'b'
salario = -1
ecivil = 'p'

while len(nome) <= 3:

        nome = input('Digite seu nome : ')



while idade not in range(0,151):

        idade = int(input('Digite sua idade : '))

while salario < 0:

       salario = int(input('Digite seu salario : '))

while sexo.upper() not in ['F','M']:

        sexo = input('Digite seu sexo com M para masculino e F para feminino : ').upper()


while ecivil.upper() not in ['S', 'C', 'V', 'D']:


        ecivil = input('Digite seu estado Civil com \nS solteiro \nC casado \nV variado da cabeça'
                       '\nD divorciado').upper()

print(f'Nome : {nome}\nIdade : {idade}\nSalario : {salario}\nSexo : {sexo}\nEstado Civil : {ecivil}')