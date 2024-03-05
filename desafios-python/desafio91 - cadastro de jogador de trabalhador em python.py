print('------ DESAFIO 91 ------')

trabalhadur = dict()

trabalhadur['nome'] = str(input('Nome: '))
trabalhadur['nascimento'] = int(input('Ano de nascimento: '))
trabalhadur['carteira'] = int(input('Carteira de Trabalho (0 não tem): '))
trabalhadur['contratação'] = str(input('Ano de Contratação: '))
trabalhadur['salário'] = int(input('Salário: R$'))

while True:

    if trabalhadur['carteira'] in 0:
        break

print('=-' * 30)

print(trabalhadur)