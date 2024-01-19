lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')

#Tuplas são imutáveis

print('-=' * 11)

print(lanche[1])
print(lanche[-2])
print(lanche[1:3])
print(lanche[2:])
print(lanche[-3:])

print('-=' * 11)

print(sorted(lanche))

print('-=' * 11)

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')

print('Comi pra caramba!')

print('-=' * 11)

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print('Comi pra caramba!')

print('-=' * 11)

for comida in lanche:
    print(f'Eu vou comer {comida}')

print('Comi pra caramba!')

print('-=' * 11)

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a

print(c)
print(len(c))
print(c.count(8))
print(c.index(1))
print(c.index(5, 0))

print('-=' * 11)