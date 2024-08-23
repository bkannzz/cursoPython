print('------ DESAFIO 54 ------')

maior = 0
menor = 0 

for pess in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(pess)))

    if pess == 1:
        maior = pess
        menor = pess
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('O maior peso lido foi de {}kg'.format(maior))
print('O menor peso lido foi de {}kg'.format(menor))