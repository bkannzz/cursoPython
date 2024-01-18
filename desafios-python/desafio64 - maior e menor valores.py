print('------ DESAFIO 64 ------')

r = 'S'
num = contagem = maior = menor = 0 

while r == 'S':
    n = int(input('Digite um valor:'))
    r = str(input('Quer continuar? [S/N] ')).upper()

    contagem += 1
    num += n
    media = num / contagem

    if contagem == 1:
        menor = n
    else:
        if n < menor:
            menor = n

print('Você digitou {} números e a média foi {:.2f}'.format(contagem, media))
print('o menor foi {}'.format(menor))