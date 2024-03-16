print('------ DESAFIO 93 ------')

pessoas = dict()
galera = list()
soma = media = 0

while True:
    pessoas.clear()
    pessoas['nome'] = str(input('Nome:'))

    while True:
        pessoas['sexo'] = str(input('Sexo: [M/F]')).upper()[0]

        if pessoas['sexo'] in 'MF':
            break
        (print('ERRO! Por favor, digite apenas M ou F.'))

    pessoas['idade'] = int(input('Idade:'))

    soma += pessoas['idade']

    galera.append(pessoas.copy())
    
    while True:
        resposta = str(input('Quer continuar? [S/N] ')).upper()[0]

        if resposta in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resposta == 'N':
        break

print('=-' * 30)
print(f'Ao todo temos {len(galera)} pessoas cadastradas')

media = soma / len(galera)

print(f'A média de idade é de {media:5.2f} anos.')
print('As mulheres cadastradas foram ', end='')

for p in galera:
    if p['sexo'] in 'F':
        print(f'{p["nome"]} ', end='')
print()
print('Lista das pessoas que estão acima da média: ')

for p in galera:
    if p['idade'] >= media:
        print('    ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()