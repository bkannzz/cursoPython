print('------ DESAFIO 57 ------')

from random import randint

computador = randint(0, 10)
tentativa = 0 
acertou = False

print('Sou seu computador...')
print('Vou pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')

while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    tentativa += 1

    if jogador == computador:
        acertou = True

    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez.')
    
        elif jogador > computador:
            print('Menos... Tente mais uma vez')
    
print('Acertou com {} tentativas. Parábens!'.format(tentativa))