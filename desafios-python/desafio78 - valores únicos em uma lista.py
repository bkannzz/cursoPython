print('------ DESAFIO 78 ------')

valores = []

while True:
    n = int(input('Digite um valor: '))

    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso...')

    else:
        print('Valor duplicado! Não vou adicionar...')

    resposta = str(input('Quer continuar? [S/N] '))

    if resposta in 'Nn':
        break

print('-=' * 30)

valores.sort()

print(f'Você digitou os valores {[-1],valores}')