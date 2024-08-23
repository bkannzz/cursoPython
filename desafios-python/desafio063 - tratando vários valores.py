print('------ DESAFIO 63 ------')

num = cont = soma = 0

while num != 999:
    num = int(input('Digite um valor: '))

    soma += num
    cont += 1
    contagem = cont - 1

print('Você digitou {} números e a soma entre eles foi {}'.format(contagem, soma - 999))