print('------ DESAFIO 69 ------')

vbarato = contagem = total = mais1k = 0
pbarato = ' '

while True:
    print('-' * 21)
    print(' LOJA SUPER BARATÃO ')
    print('-' * 21)

    produto = str(input('Nome do Produto: '))
    valor = int(input('Preço: R$'))

    contagem += 1

    total += valor

    if valor >= 1000:
        mais1k += 1

    if contagem == 1:
        vbarato = valor
        pbarato = produto

    else:
        if valor < vbarato:
            vbarato = valor
            pbarato = produto

    resposta = ' '

    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    if resposta == 'N':
        print('------------ FIM DO PROGRAMA ------------')
        print(f'O total da compra foi R${total:.2f}')
        print(f'Temos {mais1k} produtos custando mais de R$1000.00')
        print(f'O produto mais barato foi {pbarato} que custa R${vbarato}')
        break