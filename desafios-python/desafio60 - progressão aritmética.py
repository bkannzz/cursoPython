print('------ DESAFIO 60 ------')

print('Gerador de PA')
print('=-=' * 5)

numero = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))

termo = numero
contador = 1

while contador <= 10:
    print('{} -> '.format(termo), end='') 
    termo = termo + r
    contador += 1

print('FIM')
