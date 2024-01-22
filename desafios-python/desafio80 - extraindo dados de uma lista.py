print('------ DESAFIO 80 ------')

valores = []
total = 0 

while True:
    n = int(input('Digite um valor: '))

    if n not in valores:
        valores.append(n)
        total += 1

    resposta = str(input('Quer continuar? [S/N] '))

    if resposta in 'Nn':
        break

print('=-' * 30)

print(f'Você digitou {total} elementos.')

valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')

if 5 in valores:
        print('O valor 5 não faz parte da lista!')
else:
    print('O valor 5 faz parte da lista!')
