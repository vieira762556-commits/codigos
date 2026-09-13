from random import randint


def busca_sequencial(lista, valor):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i
    return -1


def existe_sequencial(lista, valor):
    return busca_sequencial(lista, valor) != -1


def busca_binaria(lista, valor):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if lista[meio] == valor:
            return meio
        if valor < lista[meio]:
            fim = meio - 1
        else:
            inicio = meio + 1

    return -1


def busca_binaria_bool(lista, valor):
    return busca_binaria(lista, valor) != -1


def busca_binaria_primeira(lista, valor):
    inicio = 0
    fim = len(lista) - 1
    resultado = -1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if lista[meio] == valor:
            resultado = meio
            fim = meio - 1
        elif valor < lista[meio]:
            fim = meio - 1
        else:
            inicio = meio + 1

    return resultado


def busca_binaria_ultima(lista, valor):
    inicio = 0
    fim = len(lista) - 1
    resultado = -1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if lista[meio] == valor:
            resultado = meio
            inicio = meio + 1
        elif valor < lista[meio]:
            fim = meio - 1
        else:
            inicio = meio + 1

    return resultado


def ler_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Digite um número inteiro válido.")


def ler_float(mensagem):
    while True:
        try:
            return float(input(mensagem).replace(",", "."))
        except ValueError:
            print("Digite uma nota válida.")


def linha():
    print("-" * 60)


def exercicio_1():
    numeros = [4, 8, 15, 16, 23, 42, 7, 11, 19, 31]
    valor = ler_inteiro("Digite um número para procurar: ")
    encontrado = False

    for numero in numeros:
        if numero == valor:
            encontrado = True
            break

    print("Lista:", numeros)
    if encontrado:
        print("O número está presente na lista.")
    else:
        print("O número não está presente na lista.")


def exercicio_2():
    nomes = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda"]
    nome = input("Digite um nome: ").strip()
    posicao = -1

    for i in range(len(nomes)):
        if nomes[i].lower() == nome.lower():
            posicao = i
            break

    if posicao != -1:
        print(f"{nome} foi encontrado na posição {posicao}.")
    else:
        print("Nome não encontrado.")


def exercicio_3():
    lista = [10, 20, 30, 40, 50]
    valor = ler_inteiro("Digite o valor procurado: ")
    indice = busca_sequencial(lista, valor)
    print("Lista:", lista)
    print("Índice encontrado:", indice)


def exercicio_4():
    notas = [7.5, 8.0, 6.5, 8.0, 9.0, 7.5, 8.0]
    nota = ler_float("Digite a nota procurada: ")
    quantidade = 0

    for item in notas:
        if item == nota:
            quantidade += 1

    if quantidade > 0:
        print(f"A nota {nota} aparece {quantidade} vez(es).")
    else:
        print("A nota não aparece na lista.")


def exercicio_5():
    produtos = ["arroz", "feijão", "macarrão", "leite", "café"]
    precos = [24.90, 8.50, 5.75, 4.99, 16.30]
    produto = input("Digite o nome do produto: ").strip().lower()
    posicao = -1

    for i in range(len(produtos)):
        if produtos[i] == produto:
            posicao = i
            break

    if posicao != -1:
        print(f"Preço de {produtos[posicao]}: R$ {precos[posicao]:.2f}")
    else:
        print("Produto não encontrado.")


def exercicio_6():
    numeros = [12, 45, 9, 67, 34, 88, 21]
    maior = numeros[0]

    for i in range(1, len(numeros)):
        if numeros[i] > maior:
            maior = numeros[i]

    print("Lista:", numeros)
    print("Maior valor:", maior)


def exercicio_7():
    numeros = [randint(1, 10) for _ in range(20)]
    valor = ler_inteiro("Digite o valor procurado: ")
    posicoes = []

    for i in range(len(numeros)):
        if numeros[i] == valor:
            posicoes.append(i)

    print("Lista:", numeros)
    if len(posicoes) > 0:
        print("Posições encontradas:", posicoes)
    else:
        print("Valor não encontrado.")


def exercicio_8():
    lista = [3, 6, 9, 12, 15]
    valor = ler_inteiro("Digite o número: ")
    print("Lista:", lista)
    print(existe_sequencial(lista, valor))


def exercicio_9():
    matriculas = [2024001, 2024002, 2024003, 2024004, 2024005]
    matricula = ler_inteiro("Digite a matrícula: ")

    if existe_sequencial(matriculas, matricula):
        print("Aluno cadastrado.")
    else:
        print("Aluno não cadastrado.")


def exercicio_10():
    palavras = ["python", "algoritmo", "dados", "universidade", "software"]
    maior_palavra = palavras[0]

    for i in range(1, len(palavras)):
        if len(palavras[i]) > len(maior_palavra):
            maior_palavra = palavras[i]

    print("Lista:", palavras)
    print("Palavra com mais caracteres:", maior_palavra)


def exercicio_11():
    cpfs = ["111.111.111-11", "222.222.222-22", "333.333.333-33", "444.444.444-44"]
    cpf = input("Digite um CPF fictício: ").strip()
    comparacoes = 0
    encontrado = False

    for item in cpfs:
        comparacoes += 1
        if item == cpf:
            encontrado = True
            break

    if encontrado:
        print("CPF cadastrado.")
    else:
        print("CPF não cadastrado.")
    print("Comparações realizadas:", comparacoes)


def exercicio_12():
    lista = [5, 12, 18, 25, 33, 47]
    valor = ler_inteiro("Digite o valor procurado: ")
    comparacoes = 0

    for i in range(len(lista)):
        comparacoes += 1
        if lista[i] == valor:
            print(f"Valor {valor} encontrado na posição {i}.")
            print("Comparações:", comparacoes)
            return

    print("Valor não encontrado.")
    print("Comparações:", comparacoes)


def exercicio_13():
    lista = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    valor = ler_inteiro("Digite o número procurado: ")
    indice = busca_binaria(lista, valor)
    print("Lista ordenada:", lista)

    if indice != -1:
        print(f"Valor encontrado na posição {indice}.")
    else:
        print("Valor não encontrado.")


def exercicio_14():
    lista = [1, 4, 7, 10, 13, 16, 19]
    valor = ler_inteiro("Digite o valor procurado: ")
    print("Índice encontrado:", busca_binaria(lista, valor))


def exercicio_15():
    nomes = ["Amanda", "Bruno", "Carla", "Diego", "Fernanda", "Lucas", "Mariana"]
    nome = input("Digite o nome procurado: ").strip()
    inicio = 0
    fim = len(nomes) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if nomes[meio].lower() == nome.lower():
            print(f"Nome encontrado na posição {meio}.")
            return
        if nome.lower() < nomes[meio].lower():
            fim = meio - 1
        else:
            inicio = meio + 1

    print("Nome não encontrado.")


def exercicio_16():
    lista = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30,
             33, 36, 39, 42, 45, 48, 51, 54, 57, 60]
    valor = ler_inteiro("Digite o valor procurado: ")
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        print(f"inicio={inicio}, fim={fim}, meio={meio}, valor_meio={lista[meio]}")

        if lista[meio] == valor:
            print(f"Valor encontrado na posição {meio}.")
            return
        if valor < lista[meio]:
            fim = meio - 1
        else:
            inicio = meio + 1

    print("Valor não encontrado.")


def exercicio_17():
    codigos = [101, 115, 129, 140, 158, 172, 190]
    codigo = ler_inteiro("Digite o código do produto: ")

    if busca_binaria(codigos, codigo) != -1:
        print("Código cadastrado.")
    else:
        print("Código não cadastrado.")


def exercicio_18():
    lista = [4, 9, 15, 23, 31, 42, 58, 64, 77]
    valor = ler_inteiro("Digite o valor procurado: ")
    inicio = 0
    fim = len(lista) - 1
    comparacoes = 0

    while inicio <= fim:
        meio = (inicio + fim) // 2
        comparacoes += 1

        if lista[meio] == valor:
            print(f"Valor encontrado na posição {meio}.")
            print("Comparações:", comparacoes)
            return
        if valor < lista[meio]:
            fim = meio - 1
        else:
            inicio = meio + 1

    print("Valor não encontrado.")
    print("Comparações:", comparacoes)


def exercicio_19():
    lista = [2, 4, 6, 8, 10, 12]
    valor = ler_inteiro("Digite o valor procurado: ")
    print(busca_binaria_bool(lista, valor))


def exercicio_20():
    pares = []
    numero = 2
    while numero <= 200:
        pares.append(numero)
        numero += 2

    valor = ler_inteiro("Digite um número: ")
    indice = busca_binaria(pares, valor)

    if indice != -1:
        print(f"Número encontrado na posição {indice}.")
    else:
        print("Número não encontrado.")


def exercicio_21():
    lista = [1, 2, 2, 2, 4, 5, 5, 7, 9]
    valor = ler_inteiro("Digite o valor procurado: ")
    indice = busca_binaria(lista, valor)
    print("Lista:", lista)

    if indice != -1:
        print(f"Uma ocorrência foi encontrada no índice {indice}.")
    else:
        print("Valor não encontrado.")


def exercicio_22():
    lista = [1, 2, 2, 2, 4, 5, 5, 7, 9]
    valor = ler_inteiro("Digite o valor procurado: ")
    print("Lista:", lista)
    print("Primeira ocorrência:", busca_binaria_primeira(lista, valor))


def exercicio_23():
    lista = [1, 2, 2, 2, 4, 5, 5, 7, 9]
    valor = ler_inteiro("Digite o valor procurado: ")
    print("Lista:", lista)
    print("Última ocorrência:", busca_binaria_ultima(lista, valor))


def exercicio_24():
    idades = [12, 15, 18, 21, 24, 30, 35, 40, 48, 60]
    idade = ler_inteiro("Digite a idade procurada: ")
    inicio = 0
    fim = len(idades) - 1
    descartados = 0

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if idades[meio] == idade:
            print(f"Idade encontrada na posição {meio}.")
            print("Elementos descartados:", descartados)
            return
        if idade < idades[meio]:
            descartados += fim - meio + 1
            fim = meio - 1
        else:
            descartados += meio - inicio + 1
            inicio = meio + 1

    print("Idade não encontrada.")
    print("Elementos descartados:", descartados)


def exercicio_25():
    codigos_livros = [1001, 1005, 1010, 1020, 1035, 1050]
    codigo = ler_inteiro("Digite o código do livro: ")
    indice = busca_binaria(codigos_livros, codigo)

    if indice != -1:
        print(f"Livro disponível na posição {indice}.")
    else:
        print("Livro indisponível ou não cadastrado.")


def exercicio_26():
    codigos = [34, 12, 78, 45, 90, 23]
    codigo = ler_inteiro("Digite o código do produto: ")

    comparacoes_seq = 0
    indice_seq = -1
    for i in range(len(codigos)):
        comparacoes_seq += 1
        if codigos[i] == codigo:
            indice_seq = i
            break

    ordenados = sorted(codigos)
    inicio = 0
    fim = len(ordenados) - 1
    comparacoes_bin = 0
    indice_bin = -1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        comparacoes_bin += 1
        if ordenados[meio] == codigo:
            indice_bin = meio
            break
        if codigo < ordenados[meio]:
            fim = meio - 1
        else:
            inicio = meio + 1

    print("Lista original:", codigos)
    print("Lista ordenada para busca binária:", ordenados)
    print("Resultado sequencial:", indice_seq, "| comparações:", comparacoes_seq)
    print("Resultado binário:", indice_bin, "| comparações:", comparacoes_bin)


def exercicio_27():
    matriculas = [2024007, 2024002, 2024010, 2024001, 2024005]
    print("1 - Busca sequencial")
    print("2 - Busca binária")
    opcao = ler_inteiro("Escolha o tipo de busca: ")
    matricula = ler_inteiro("Digite a matrícula: ")

    if opcao == 1:
        indice = busca_sequencial(matriculas, matricula)
        print("Lista original:", matriculas)
    elif opcao == 2:
        matriculas = sorted(matriculas)
        indice = busca_binaria(matriculas, matricula)
        print("Lista ordenada:", matriculas)
    else:
        print("Opção inválida.")
        return

    if indice != -1:
        print(f"Matrícula encontrada na posição {indice}.")
    else:
        print("Matrícula não encontrada.")


def exercicio_28():
    lista = []
    for numero in range(1, 1001):
        lista.append(numero)

    valor = 1000
    comparacoes_seq = 0
    for item in lista:
        comparacoes_seq += 1
        if item == valor:
            break

    inicio = 0
    fim = len(lista) - 1
    comparacoes_bin = 0
    while inicio <= fim:
        meio = (inicio + fim) // 2
        comparacoes_bin += 1

        if lista[meio] == valor:
            break
        if valor < lista[meio]:
            fim = meio - 1
        else:
            inicio = meio + 1

    print("Valor procurado:", valor)
    print("Comparações na busca sequencial:", comparacoes_seq)
    print("Comparações na busca binária:", comparacoes_bin)
    print("Conclusão: em lista ordenada grande, a busca binária é mais eficiente.")


def exercicio_29():
    nomes = ["Ana", "Bruno", "Carla", "Daniel", "Eduarda", "Felipe", "Marina"]
    telefones = ["9999-1001", "9999-1002", "9999-1003", "9999-1004",
                 "9999-1005", "9999-1006", "9999-1007"]
    nome = input("Digite o nome do contato: ").strip()
    inicio = 0
    fim = len(nomes) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if nomes[meio].lower() == nome.lower():
            print(f"Contato encontrado: {nomes[meio]} - {telefones[meio]}")
            return
        if nome.lower() < nomes[meio].lower():
            fim = meio - 1
        else:
            inicio = meio + 1

    print("Contato não encontrado.")


def ordenar_lista(lista):
    ordenada = lista[:]
    for i in range(len(ordenada)):
        for j in range(0, len(ordenada) - 1 - i):
            if ordenada[j] > ordenada[j + 1]:
                auxiliar = ordenada[j]
                ordenada[j] = ordenada[j + 1]
                ordenada[j + 1] = auxiliar
    return ordenada


def exercicio_30():
    valores = []
    ordenada = False

    while True:
        linha()
        print("1 - Cadastrar valores")
        print("2 - Exibir lista")
        print("3 - Ordenar lista")
        print("4 - Realizar busca sequencial")
        print("5 - Realizar busca binária")
        print("0 - Sair")
        opcao = ler_inteiro("Escolha: ")

        if opcao == 1:
            valor = ler_inteiro("Digite um valor para cadastrar: ")
            valores.append(valor)
            ordenada = False
            print("Valor cadastrado.")
        elif opcao == 2:
            print("Lista:", valores)
        elif opcao == 3:
            valores = ordenar_lista(valores)
            ordenada = True
            print("Lista ordenada:", valores)
        elif opcao == 4:
            valor = ler_inteiro("Digite o valor procurado: ")
            indice = busca_sequencial(valores, valor)
            if indice != -1:
                print(f"Valor encontrado na posição {indice}.")
            else:
                print("Valor não encontrado.")
        elif opcao == 5:
            if not ordenada:
                print("A busca binária só pode ser feita depois de ordenar a lista.")
            else:
                valor = ler_inteiro("Digite o valor procurado: ")
                indice = busca_binaria(valores, valor)
                if indice != -1:
                    print(f"Valor encontrado na posição {indice}.")
                else:
                    print("Valor não encontrado.")
        elif opcao == 0:
            break
        else:
            print("Opção inválida.")

EXERCICIOS = {
    1: exercicio_1,
    2: exercicio_2,
    3: exercicio_3,
    4: exercicio_4,
    5: exercicio_5,
    6: exercicio_6,
    7: exercicio_7,
    8: exercicio_8,
    9: exercicio_9,
    10: exercicio_10,
    11: exercicio_11,
    12: exercicio_12,
    13: exercicio_13,
    14: exercicio_14,
    15: exercicio_15,
    16: exercicio_16,
    17: exercicio_17,
    18: exercicio_18,
    19: exercicio_19,
    20: exercicio_20,
    21: exercicio_21,
    22: exercicio_22,
    23: exercicio_23,
    24: exercicio_24,
    25: exercicio_25,
    26: exercicio_26,
    27: exercicio_27,
    28: exercicio_28,
    29: exercicio_29,
    30: exercicio_30,
}


def menu_principal():
    while True:
        linha()
        print("LISTA 3 - ALGORITMOS DE BUSCA EM PYTHON")
        print("Digite um número de 1 a 30 para executar um exercício.")
        print("31 - Ver reflexão final")
        print("0 - Sair")
        opcao = ler_inteiro("Escolha: ")

        if opcao == 0:
            print("Programa encerrado.")
            break
        elif opcao in EXERCICIOS:
            linha()
            print(f"Exercício {opcao}")
            EXERCICIOS[opcao]()
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu_principal()
