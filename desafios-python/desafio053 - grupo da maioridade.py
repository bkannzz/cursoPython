print('------ DESAFIO 53 ------')

maior = 0
menor = 0

for pess in range(1, 8):
    anos = int(input('Em que ano a {}ª pessoa nasceu? '.format(pess)))
    
    idade = 2024 - anos
    if idade >= 18:
        maior += 1
    else:
        menor += 1

print('Ao todo tivemos {} pessoas maiores de idade'.format(maior))
print('E também tivemos {} pessoas menores de idade'.format(menor))
