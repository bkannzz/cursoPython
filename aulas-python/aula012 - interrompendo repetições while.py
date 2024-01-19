n = s = 0 
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}')

nome = 'Rebecca'
idade = 16
salario = 987.3

print(f'Seu nome é {nome} e você tem {idade} anos e ganha R${salario:.2f}')