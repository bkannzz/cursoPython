def titulo(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)

# PROGRAMA PRINCIPAL
    
titulo('     CURSO EM VIDEO      ')
 
titulo('     APRENDA PYTHON      ')

titulo('     GUSTAVO GUANABARA   ')

def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')

# PROGRAMA PRINCIPAL
    
soma(4, 5)

print('-' * 30)

# SOMAR QUANTIDADE DE NÚMEROS

def contador(* num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números')

contador(2, 1, 7)
contador(6, 4, 1, 6)
contador(2, 1, 9, 4, 8)

print('-' * 30)

# DOBRAR OS NÚMEROS

def dobra(lst):
    pos = 0 
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1 

valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)

print('-' * 30)

# SOMAR TODOS OS NÚMEROS

def soma(* valores):
    s = 0 
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')

soma(5, 2)
