print('------ DESAFIO 22 ------')

num = int(input('Digite um número de quatro digitos: '))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

if num <= 9999:
    print('Analisando o número {}'.format(num))
    print('Unidade: {}'.format(u))
    print('Dezena: {}'.format(d))
    print('Centena: {}'.format(c))
    print('Milhar: {}'.format(m))
    
else:
    print('Número inválido! Tente novamente.')
