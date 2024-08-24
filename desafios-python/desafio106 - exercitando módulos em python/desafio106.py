print('------ DESAFIO 106 ------')

import moeda

res = float(input('Digite o preço R$'))
print(f'A metade de R${res} é R${moeda.metade(res)}')
print(f'O dobro de R{res} é R${moeda.dobro(res)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(res, 10)}')