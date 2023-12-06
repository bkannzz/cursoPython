print('------ DESAFIO 12 ------')

preco = float(input('Digite o preço de um produto: '))

conta = preco * 5 / 100
desconto = preco - conta

print('O novo preço do produto com 5% de desconto será R${:.2f}'.format(desconto))