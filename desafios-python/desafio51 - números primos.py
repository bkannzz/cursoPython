print('------ DESAFIO 51 ------')

numero = int(input('Digite um número: '))

tot = 0 

for c in range(1, numero):
    if numero % c == 0:
        tot += 1
    print('{} '.format(c), end='')

if tot == 2:
    print('\nele é PRIMO!')

else:
    print('\nele NÃO É PRIMO!')