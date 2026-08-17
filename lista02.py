# Exercício 1
def exibir_primeiro_terceiro_ultimo(lista):
    print("Primeiro elemento:", lista[0])
    print("Terceiro elemento:", lista[2])
    print("Último elemento:", lista[-1])
    print("Quantidade de elementos:", len(lista))


# Exercício 2
def percorrer_lista(lista):
    print("Elementos da lista:")
    for elemento in lista:
        print(elemento)

    print("Valores maiores que 10:")
    for elemento in lista:
        if elemento > 10:
            print(elemento)


# Exercício 3
def calcular_soma(lista):
    soma = 0
    for numero in lista:
        soma += numero
    print("Soma dos elementos:", soma)


# Exercício 4
def calcular_media(notas):
    total = 0
    for nota in notas:
        total += nota
    media = total / len(notas)
    print(f"Média: {media:.2f}")


# Exercício 5
def maior_menor_valor(lista):
    maior = lista[0]
    menor = lista[0]

    for numero in lista[1:]:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

    print("Maior valor:", maior)
    print("Menor valor:", menor)


# Exercício 6
def ex6_contagem_pares_impares(lista):
    pares = 0
    impares = 0

    for numero in lista:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1

    print("Quantidade de pares:", pares)
    print("Quantidade de ímpares:", impares)


# Exercício 7
def ex7_busca_elemento():
    lista = []

    for posicao in range(8):
        numero = int(input(f"Digite o {posicao + 1}º número: "))
        lista.append(numero)

    busca = int(input("Digite o número para pesquisar: "))
    encontrado = False

    for numero in lista:
        if numero == busca:
            encontrado = True
            break

    if encontrado:
        print("O número está na lista.")
    else:
        print("O número não está na lista.")


# Exercício 8
def ex8_posicao_elemento():
    nomes = ["Ana", "Bruno", "Carlos", "Daniel", "Eduarda"]
    nome = input("Digite o nome para localizar: ")
    posicao = -1

    for indice, valor in enumerate(nomes):
        if valor == nome:
            posicao = indice
            break

    if posicao != -1:
        print(f"O nome {nome} está na posição {posicao}.")
    else:
        print("Nome não encontrado.")


# Exercício 9
def ex9_insercao_remocao():
    lista = []

    for posicao in range(5):
        numero = int(input(f"Digite o {posicao + 1}º número: "))
        lista.append(numero)

    print("Lista antes da remoção:", lista)

    numero_para_remover = int(input("Digite um número para remover: "))
    nova_lista = []
    removido = False

    for numero in lista:
        if numero == numero_para_remover and not removido:
            removido = True
        else:
            nova_lista.append(numero)

    print("Lista depois da remoção:", nova_lista)


# Exercício 10
def ex10_ordenacao():
    numeros = [18, 5, 12, 3, 20, 7, 9]
    print("Lista original:", numeros)

    crescente = sorted(numeros)
    print("Ordem crescente:", crescente)

    numeros.sort(reverse=True)
    print("Ordem decrescente:", numeros)


# Exercício 11
def ex11_fatiamento():
    valores = [10, 20, 30, 40, 50, 60, 70, 80]
    print("Primeiros 4 elementos:", valores[:4])
    print("Últimos 3 elementos:", valores[-3:])
    print("Elementos das posições 2 a 5:", valores[2:6])
    print("Lista invertida:", valores[::-1])


# Exercício 12
def ex12_lista_sem_repeticao():
    numeros = [2, 5, 2, 8, 5, 9, 2, 8, 10]
    sem_repeticao = []

    for numero in numeros:
        if numero not in sem_repeticao:
            sem_repeticao.append(numero)

    print("Lista sem repetição:", sem_repeticao)


# Exercício 13
def ex13_valores_acima_da_media():
    numeros = []

    for posicao in range(10):
        numero = float(input(f"Digite o {posicao + 1}º número: "))
        numeros.append(numero)

    total = 0
    for numero in numeros:
        total += numero

    media = total / len(numeros)
    acima_media = []

    for numero in numeros:
        if numero > media:
            acima_media.append(numero)

    print("Média:", media)
    print("Valores acima da média:", acima_media)


# Exercício 14
def ex14_compreensao_de_listas():
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    quadrados = [numero ** 2 for numero in numeros]
    pares = [numero for numero in numeros if numero % 2 == 0]
    maiores_que_5 = [numero for numero in numeros if numero > 5]

    print("Quadrados:", quadrados)
    print("Pares:", pares)
    print("Maiores que 5:", maiores_que_5)


# Exercício 15
def ex15_listas_paralelas():
    alunos = ["Ana", "Bruno", "Carlos", "Daniel", "Eduarda"]
    notas = [7.5, 8.0, 5.5, 6.0, 9.0]

    for aluno, nota in zip(alunos, notas):
        situacao = "Aprovado" if nota >= 6 else "Reprovado"
        print(f"Aluno: {aluno} | Nota: {nota} | Situação: {situacao}")


# Exercício 16
def ex16_lista_de_listas():
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    soma_total = 0
    somas_linhas = []

    for linha in matriz:
        soma_linha = 0
        for valor in linha:
            print(valor, end=" ")
            soma_total += valor
            soma_linha += valor
        print()
        somas_linhas.append(soma_linha)

    print("Soma de todos os valores:", soma_total)
    print("Soma de cada linha:", somas_linhas)


# Exercício 17
def ex17_segundo_maior_valor_distinto(lista):
    maior = None
    segundo_maior = None

    for numero in lista:
        if maior is None or numero > maior:
            segundo_maior = maior
            maior = numero
        elif numero != maior and (segundo_maior is None or numero > segundo_maior):
            segundo_maior = numero

    print("Segundo maior valor distinto:", segundo_maior)


# Exercício 18
def ex18_frequencia_elementos(lista):
    frequencia = {}

    for numero in lista:
        if numero in frequencia:
            frequencia[numero] += 1
        else:
            frequencia[numero] = 1

    for numero, quantidade in frequencia.items():
        print(f"{numero} aparece {quantidade} vez(es).")


# Exercício 19
def ex19_controle_estoque():
    produtos = ["Teclado", "Mouse", "Monitor", "Notebook", "Headset"]
    quantidades = [12, 25, 4, 3, 8]

    while True:
        print("\n=== Controle de estoque ===")
        print("1 - Consultar produto")
        print("2 - Alterar quantidade")
        print("3 - Produtos com estoque abaixo de 5")
        print("4 - Produto com maior quantidade")
        print("0 - Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            nome = input("Digite o nome do produto: ")
            for indice, produto in enumerate(produtos):
                if produto == nome:
                    print(f"{produto}: {quantidades[indice]} unidade(s)")
                    break
            else:
                print("Produto não encontrado.")

        elif opcao == 2:
            nome = input("Digite o nome do produto: ")
            nova_quantidade = int(input("Digite a nova quantidade: "))
            for indice, produto in enumerate(produtos):
                if produto == nome:
                    quantidades[indice] = nova_quantidade
                    print("Quantidade atualizada.")
                    break
            else:
                print("Produto não encontrado.")

        elif opcao == 3:
            print("Produtos com estoque inferior a 5:")
            for produto, quantidade in zip(produtos, quantidades):
                if quantidade < 5:
                    print(produto, quantidade)

        elif opcao == 4:
            maior_quantidade = quantidades[0]
            produto_maior = produtos[0]
            for indice, quantidade in enumerate(quantidades):
                if quantidade > maior_quantidade:
                    maior_quantidade = quantidade
                    produto_maior = produtos[indice]
            print(f"Produto com maior quantidade: {produto_maior} ({maior_quantidade})")

        elif opcao == 0:
            break
        else:
            print("Opção inválida.")


# Exercício 20
def ex20_analise_vendas():
    vendas = [1250, 980, 1430, 2100, 1750, 890, 1620]

    total = 0
    maior = vendas[0]
    menor = vendas[0]

    for valor in vendas:
        total += valor
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor

    media = total / len(vendas)
    dias_acima_da_media = 0

    for valor in vendas:
        if valor > media:
            dias_acima_da_media += 1

    percentual = (dias_acima_da_media / len(vendas)) * 100

    print("Total vendido:", total)
    print(f"Média diária: {media:.2f}")
    print("Maior venda:", maior)
    print("Menor venda:", menor)
    print("Dias acima da média:", dias_acima_da_media)
    print(f"Percentual de dias acima da média: {percentual:.2f}%")


# Chamada dos exercícios com execução direta
if __name__ == "__main__":
    exibir_primeiro_terceiro_ultimo([10, 20, 30, 40, 50])
    print()
    percorrer_lista([7, 12, 5, 18, 3, 20])
    print()
    calcular_soma([3, 8, 12, 5, 20, 7, 15, 9])
    print()
    calcular_media([7.5, 8.0, 6.0, 9.5, 5.5])
    print()
    maior_menor_valor([15, 4, 22, 9, 31, 12, 7])
    print()

    ex6_contagem_pares_impares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print()
    ex10_ordenacao()
    print()
    ex11_fatiamento()
    print()
    ex12_lista_sem_repeticao()
    print()
    ex14_compreensao_de_listas()
    print()
    ex15_listas_paralelas()
    print()
    ex16_lista_de_listas()
    print()
    ex17_segundo_maior_valor_distinto([12, 8, 20, 15, 20, 7, 9])
    print()
    ex18_frequencia_elementos([2, 3, 2, 5, 3, 2])
    print()
    ex20_analise_vendas()

