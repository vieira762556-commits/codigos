# Operações matematicas
def ex1():

    n1 = float(input('Digite o primeiro número:'))
    n2 = float(input('Digite o segundo número:'))

    soma = n1 + n2 
    sub = n1 - n2 
    mult = n1 * n2

    if n2 != 0 :
        div = n1 / n2
    else:
     div = 'Não e possivel por zero!'

    print(f'Soma{soma}')
    print(f'Subtração{sub}')
    print(f'Multiplicação{mult}')
    print(f'divisão{div}')

#nome e idade
def ex2():    
    nm = str(input('Digite seu nome:'))
    id = int(input('Digite sua idade:'))

    print(f'Nome do usuario: {nm}')
    print(f'Idade do usuario: {id}')

#positivo, negativo ou zero
def ex3():
    num = float(input('Digite um numero:'))

    if num > 0:
        print('O numero digitado é positivo.')
    elif num < 0:
        print('O numero digitado é negativo.')
    else:
        print('O numero digitado é zero')

#aprovado ou reprovado
def ex4():
    nt = float(input('Digite a nota do aluno:'))
    if nt >= 7: 
        print('Aprovado!!!')
    else:
        print('Reprovado!!!')

#tabuada
def ex5():
    n= int(input('Digite um numero inteiro:'))
    for i in (1,11):
        print(f'{n}x{i:<2}={n*i}')

#calculo da soma dos numeros ate n
def ex6():
    n = int(input('Digite um numero interio positivo:'))
    s = 0
    for i in(1,n+1):
        s += i
        print(f'Asoma dos números entre 1 e {n} é:{s}')

#numeros, soma e media
def ex7():
    num = []
    for i in (1, 11):
        num.append(int(input(f'Digite um {i}° número:')))
        print(f'A soma entre os números{num}é:  {sum(num)}')
        print(f'A média entre os números{num}é: {sum(num)/len(num)}')

#valores digitados
def ex8():
    j = 1
    s = 0
    c = 1
    while x != 0:
        x = int(input(f'Digite o {c}° número a ser somado [0 para encerrar]:'))
        c += 1 
        if x == 0:
            print(f'A soma de todosos valores digitados é: {s}')
            continue
        s +=j
        print(f'A soma de todos os valores digitados é {s}')

#função de dois numeros 
def ex9():
    a = int(input('Digite um número inteiro:'))
    b = int(input('Digite outro número inteiro:'))
    print(f'O maior número entre {a} e {b} é:{max(a,b)}')

#leitura de 5 numeros (maior e menor )
def ex10 ():
    x = []
    for i in (1, 6):
            x.append(int(float(f'Digite o {i}º número:')))
    print(f'O menor número em {x}é: {min(*x)}')
    print(f'O maior número em {x}é: {max(*x)}')
# def do 10
def min(*x):
    return min(x)
#def do ex 9 e 10
def max(*x):
    return max(x)
