print('------ DESAFIO 17 ------')

from math import sqrt, floor 

num1 = int(input('Digite o cateto oposto: '))
num2 = int(input('Digite o cateto adjacente: '))

soma1 = num1 * num1
soma2 = num2 * num2
somafinal = soma1 + soma2
final = sqrt(somafinal)

print('O cateto oposto tem {} e o cateto adjacente tem {}'.format(num1, num2))
print('A soma entre eles multiplicando é {}'.format(somafinal))
print('E o valor da hipotenusa é {}'.format(floor(final)))