print('------ DESAFIO 31 ------')

ano = int(input('Digite um ano: '))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano que você digitou é BISSEXTO!') 
    
else:
    print('O ano que você digitou não é bissexto!')