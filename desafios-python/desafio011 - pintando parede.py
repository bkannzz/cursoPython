print('------ DESAFIO 11 ------')

n1 = float(input('Qual é a largura da sua parede: '))
n2 = float(input('Qual é a altura da sua parede: '))

area = n1 * n2
tinta = area / 2

print('A área calculada foi de {}m² \nVocê precisará de {}l de tinta para pintar toda área.'.format(area, tinta))