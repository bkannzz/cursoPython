print('------ DESAFIO 81 ------')

total = []
par = []
impar = []

while True:
    n = int(input('Digite um valor: '))

    if n not in total:
        total.append(n)
    
    if n % 2 == 0:
        par.append(n)

    else: 
        impar.append(n)

    resposta = str(input('Quer continuar? [S/N] '))

    if resposta in 'Nn':
        break

print('=-' * 30)
print(f'A lista completa é {total}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')