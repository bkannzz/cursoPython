print('------ DESAFIO 102 ------')

def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')

nome = str(input('Nome do Jogador: '))
gols = input('Número de Gols: ')

if gols.isnumeric():
    gols = int(gols)

else:
    gols = 0

if nome.strip() == '':
    ficha(gols)

else:
    ficha(nome, gols)
