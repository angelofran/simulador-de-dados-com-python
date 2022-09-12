from random import randint
def cabeçalho(msg):
    print('~' * 45)
    print(f'{msg}'.center(45))
    print('~' * 45)

cabeçalho('Girar Dado')
pergunta = str(input('Olá, você quer jogar ao gira dados? [S/N] ')).upper().strip()[0]
if pergunta in 'S':
    while pergunta in 'S':
        try:
            número = randint(1, 7)
            print(f'O número sorteado foi {número}')
            resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
            if resp in 'N':
                print('Programa Finalizado')
                break
        except Exception as erros:
            print(f'Ouve um erro da classe: {erros.__class__}, por favor reinicie o programa!')
            break
if pergunta in 'N':
    print('Ok, você não quer jogar!')
