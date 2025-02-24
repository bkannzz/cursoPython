print('------ DESAFIO 76 ------')

vogais = ''

palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')

for pos in palavras:
    
    print(f'\nNa palavra {pos} temos ', end='')

    for letra in pos:
        if letra.lower() in 'aeiou':
            print(letra, end='')

