print('------ DESAFIO 41 ------')

print('Analisador de Triângulo')

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('terceiro segmento: '))

if r1 == r2 == r3:
    print('EQUILÁTERO: Todos os lados iguais')
elif r1 == r2 or r1 == r3 or r2 == r1 or r2 == r3 or r3 == r1: 
    print('ISÓSCELES: Dois lados iguais')
else:
    print('ESCALENO: Todos os lados diferentes')
#if r1 == r2 == r3 and r2 == r1 == r3 and r3 == r1 == r2:
