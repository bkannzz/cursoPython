print('------ DESAFIO 18 ------')

import math
angulo = float(input('Digite o ângulo que voce deseja: '))

seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(angulo, tangente))