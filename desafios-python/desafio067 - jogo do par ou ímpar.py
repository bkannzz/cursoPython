print('------ DESAFIO 67 ------')

from random import randint

computador = randint(0, 10)
vezes = 0

print('=-=' * 10)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-=' * 10)

while True:
    jogador = int(input('Digite um valor:'))

    total = jogador + computador
    tipo = ' '
    
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar [P/I]')).strip().upper()[0]

        print(f'Você jogou {jogador} e o computador {computador}. Total de {total}')

    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            vezes += 1

        else:
            print('Você PERDEU!')
            break

    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            vezes += 1

        else:
            print('Você PERDEU!')
            break
        
    print('Vamos jogar novamente.')

print(f'GAME OVER! Você venceu {vezes} vezes.')

    