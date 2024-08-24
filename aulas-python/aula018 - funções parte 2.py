# EX: DOCSTRING

def contador(i, f, p):
    """
    -> Faz uma contagem e mostrar na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')

contador(0, 100, 10)

help(contador)

print('-' * 30)

# EX: PARÂMETRO OPCIONAL

def somar(a=0, b=0, c=0):

    s = a + b + c
    print(f'A soma vale {s}')

somar(c=3, a=2)

print('-' * 30)

# EX: ESCOPO DE VARIÁVEL

def teste():
    x = 8 # VARIÁVEL LOCAL (SÓ FUNCIONA AQUI DENTRO DA FUNÇÃO)
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')

n = 2 # VARIÁVEL GLOBAL (FUNCIONA DENTRO DA FUNÇÃO TAMBÉM) 
print(f'No programa principal, "n" vale {n}')
teste()

print('-' * 30)

# EX: RETORNANDO VALORES

def fatorial(num = 1):
    f = 1
    for c in range(num, 1, -1):
        f *= c
    return f

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial(1)

print(f'Os resultados dos fatoriais são {f1}, {f2}, {f3}.')