print('------ DESAFIO 25 ------')

frase = str(input('Digite qualquer coisa: ')).upper().strip()

print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A') + 1))
print('A ultima letra A apareceu na posição {}'.format(frase.rfind('A') + 1))

 