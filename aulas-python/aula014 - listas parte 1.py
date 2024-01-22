num = [2, 5, 9 ,1]

num[2] = 3 # posição 2 receber o valor 3
num.append(7) # adicionar novo numero
num.sort(reverse=True) # organizar na ordem ao contrario
num.insert(2, 2) # colocar um numero em tal posição
num.pop() # remover o ultimo valor
num.remove(2) # remover o primeiro numero 2 que aparecer

if 5 in num:
    num.remove(5)
    print('REMOVIDO!')
else:
    print('Não achei o número 5')

print(num)
print(f'Essa lista tem {len(num)} elementos.')

valores = []
valores.append(5)
valores.append(9)
valores.append(4)

print('-=' * 13)

valores = list()

for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')

print('-=' * 13)

a = [2, 3, 4, 7]
b = a
b[2] = 8 # as duas listas ficaram ligadas, entao as duas receberão o valor

print(f'Lista A: {a}')
print(f'Lista A: {b}')

print('-=' * 13)

a = [2, 3, 4, 7]
b = a[:] # aqui somente o valor b receberá o valor
b[2] = 8 

print(f'Lista A: {a}')
print(f'Lista A: {b}')