
senha = 'a'
usuario = 'a'
while usuario == senha:
    usuario = input('Digite o seu usuario : ')
    senha = input('Digite a sua senha : ')

    if usuario == senha:
        print('usuario e senha iguais digite novamente!!!')
    else:
        print('Registro completo!')