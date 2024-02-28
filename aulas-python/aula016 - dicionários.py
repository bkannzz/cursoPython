pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}

pessoas['nome'] = 'Leandro'
pessoas['peso'] = 98.5

for k, v in pessoas.items():
    print(f'{k} = {v}')

print('=-' * 20)

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}

brasil.append(estado1)
brasil.append(estado2)

print(brasil)

estado = dict()
brasil = list()

for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))

    brasil.append(estado.copy())

for e in brasil:
    for v, f in e.items():
        print(f'O campo {v} tem valor {f}.')
    print()