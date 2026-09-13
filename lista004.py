# 1. Função recursiva para calcular o MDC de dois números inteiros

def mdc(a, b):
    if b == 0:
        return a
    else:
        return mdc(b, a % b)


# 2. Função recursiva para calcular x elevado a n

def potencia(x, n):
    if n == 0:
        return 1
    else:
        return x * potencia(x, n - 1)


# 3. Função recursiva para inverter uma string

def inverter_string(texto):
    if texto == "":
        return ""
    else:
        return inverter_string(texto[1:]) + texto[0]


# 4. Função recursiva para verificar se uma string é palíndromo

def eh_palindromo(texto):
    texto = texto.replace(" ", "").lower()

    if len(texto) <= 1:
        return True

    if texto[0] != texto[-1]:
        return False

    return eh_palindromo(texto[1:-1])


# 5. Função recursiva para calcular a soma dos dígitos

def soma_digitos(numero):
    if numero < 10:
        return numero
    else:
        return numero % 10 + soma_digitos(numero // 10)


# 6. Função recursiva para encontrar todos os anagramas de uma string

def anagramas(texto):
    if len(texto) <= 1:
        return [texto]

    resultado = []

    for i in range(len(texto)):
        letra = texto[i]
        resto = texto[:i] + texto[i+1:]

        for palavra in anagramas(resto):
            resultado.append(letra + palavra)

    return resultado