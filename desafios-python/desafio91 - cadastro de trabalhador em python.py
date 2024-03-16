print('------ DESAFIO 91 ------')

from datetime import datetime

trabalhadur = dict()

trabalhadur['nome'] = str(input('Nome: '))

nasc = int(input('Ano de Nascimento: '))

trabalhadur['idade'] = datetime.now().year - nasc
trabalhadur['carteira'] = int(input('Carteira de Trabalho (0 não tem): '))

if trabalhadur['carteira'] != 0:

    trabalhadur['contratação'] = int(input('Ano de Contratação: '))
    trabalhadur['salário'] = int(input('Salário: R$'))
    trabalhadur['aposentadoria'] = trabalhadur['idade'] + ((trabalhadur['contratação'] + 35) - datetime.now().year)

print('=-' * 30)

for k , v in trabalhadur.items():
    print(f' - {k} tem valor: {v}')