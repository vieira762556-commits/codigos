
def lê_matriz():
    M = []
    while True:
        temp = input().split()         
        if temp == []:                 
            return M
        linha = []
        for i in temp:
            linha.append(int(i))        
        M.append(linha)

def dimensões(M):
    linhas = len(M)
    if linhas == 0:                    
        return ()
    colunas = len(M[0])
    for i in range(1, linhas):
        if len(M[i]) != colunas:        
            return ()
    return (linhas, colunas)


def imprime_matriz(M):
    for linha in M:
        aux = [str(i) for i in linha]  
        print(" ".join(aux))            



def transposta(M):
    T = []
    dim = dimensões(M)
    if dim == ():
        return T
    (linhas, colunas) = dim
    for j in range(colunas):           
        linha = []
        for i in range(linhas):
            linha.append(M[i][j])
        T.append(linha)
    return T


def soma(A, B):
    C = []
    dim_a = dimensões(A)
    dim_b = dimensões(B)
    if dim_a == () or dim_a != dim_b:   
        return C
    (linhas, colunas) = dim_a
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(A[i][j] + B[i][j])
        C.append(linha)
    return C



def produto(A, B):
    dim_a = dimensões(A)
    dim_b = dimensões(B)
    if dim_a == () or dim_b == ():
        return []
    (linhas_a, colunas_a) = dim_a
    (linhas_b, colunas_b) = dim_b
    if colunas_a != linhas_b:          
        return []

    C = []
    for i in range(linhas_a):
        linha = []
        for j in range(colunas_b):
            soma_prod = 0
            for k in range(colunas_a):
                soma_prod += A[i][k] * B[k][j]
            linha.append(soma_prod)
        C.append(linha)
    return C



def é_quadrada(M):
    dim = dimensões(M)
    return dim != () and dim[0] == dim[1]



def é_diagonal(M):
    if not é_quadrada(M):
        return False
    n = len(M)
    for i in range(n):
        for j in range(n):
            if i != j and M[i][j] != 0:
                return False
    return True

def é_triangular_inferior(M):
    if not é_quadrada(M):
        return False
    n = len(M)
    for i in range(n):
        for j in range(i + 1, n):       
            if M[i][j] != 0:
                return False
    return True


def é_triangular_superior(M):
    if not é_quadrada(M):
        return False
    n = len(M)
    for i in range(1, n):
        for j in range(i):              
            if M[i][j] != 0:
                return False
    return True


def é_quadrado_mágico(M):
    if not é_quadrada(M):
        return False
    n = len(M)
    números = []
    for linha in M:
        for x in linha:
            números.append(x)
    if sorted(números) != list(range(1, n * n + 1)):
        return False
    alvo = sum(M[0])

    for i in range(n):
        soma_linha = 0
        soma_coluna = 0
        for j in range(n):
            soma_linha += M[i][j]
            soma_coluna += M[j][i]      
        if soma_linha != alvo or soma_coluna != alvo:
            return False

    diag_principal = 0
    diag_secundária = 0
    for i in range(n):
        diag_principal += M[i][i]
        diag_secundária += M[i][n - 1 - i]
    return diag_principal == alvo and diag_secundária == alvo



def é_matriz_permutação(M):
    if not é_quadrada(M):
        return False
    n = len(M)
    for i in range(n):
        uns_linha = 0
        uns_coluna = 0
        for j in range(n):
            if M[i][j] != 0 and M[i][j] != 1:   
                return False
            uns_linha += M[i][j]
            uns_coluna += M[j][i]
        if uns_linha != 1 or uns_coluna != 1:
            return False
    return True



def lê_matriz_com_aviso(nome="a matriz"):
    print(f"Digite {nome}, uma linha por vez, números separados por espaço.")
    print("(Linha em branco para terminar)")
    return lê_matriz()


def mostra_resultado_bool(nome, resultado):
    if resultado:
        print(f"-> É {nome}.")
    else:
        print(f"-> NÃO é {nome}.")


def testa_todos_os_exemplos():
    """Roda os exercícios e mostra OK ou ERRO para cada um."""

    def confere(descrição, obtido, esperado):
        status = "OK  " if obtido == esperado else "ERRO"
        print(f"[{status}] {descrição}")
        if obtido != esperado:
            print(f"        esperado: {esperado}")
            print(f"        obtido:   {obtido}")

    # Ex. 2
    confere("Ex. 2 - matriz 2x3", dimensões([[1, 2, 3], [4, 5, 6]]), (2, 3))
    confere("Ex. 2 - não é matriz", dimensões([[1, 2, 3], [4, 5]]), ())

    # Ex. 3 (só mostra na tela)
    print("Ex. 3 - impressão de [[1, 2, 3], [4, 5, 6]]:")
    imprime_matriz([[1, 2, 3], [4, 5, 6]])

    # Ex. 4
    M = [[1, 2, 3, 4], [5, 6, 7, 8]]
    confere("Ex. 4 - transposta", transposta(M),
            [[1, 5], [2, 6], [3, 7], [4, 8]])

    # Ex. 5
    A = [[1, 2], [3, 4], [5, 6]]
    B = [[5, 6], [1, 3], [4, 2]]
    confere("Ex. 5 - soma", soma(A, B), [[6, 8], [4, 7], [9, 8]])
    confere("Ex. 5 - soma incompatível", soma(A, [[1, 2]]), [])

    # Ex. 6
    confere("Ex. 6 - produto", produto([[1, 2], [3, 4]], [[5], [6]]),
            [[17], [39]])
    confere("Ex. 6 - produto incompatível",
            produto([[1, 2], [3, 4]], [[1, 2, 3]]), [])

    # Ex. 7
    diagonal = [[1, 0, 0, 0, 0],
                [0, 5, 0, 0, 0],
                [0, 0, 4, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 3]]
    confere("Ex. 7 - é diagonal", é_diagonal(diagonal), True)
    confere("Ex. 7 - não é diagonal", é_diagonal([[1, 2], [0, 1]]), False)

    # Ex. 8
    inferior = [[1, 0, 0, 0, 0],
                [0, 5, 0, 0, 0],
                [0, 4, 4, 0, 0],
                [0, 1, 0, 0, 0],
                [0, 9, 0, 2, 3]]
    confere("Ex. 8 - é triangular inferior", é_triangular_inferior(inferior), True)
    confere("Ex. 8 - não é triangular inferior",
            é_triangular_inferior([[1, 2], [0, 1]]), False)

    # Ex. 9
    superior = [[1, 0, 8, 9, 8],
                [0, 5, 0, 0, 0],
                [0, 0, 4, 0, 7],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 3]]
    confere("Ex. 9 - é triangular superior", é_triangular_superior(superior), True)
    confere("Ex. 9 - não é triangular superior",
            é_triangular_superior([[1, 0], [2, 1]]), False)

    # Ex. 10
    mágico = [[15, 8, 1, 24, 17],
              [16, 14, 7, 5, 23],
              [22, 20, 13, 6, 4],
              [3, 21, 19, 12, 10],
              [9, 2, 25, 18, 11]]
    confere("Ex. 10 - é quadrado mágico", é_quadrado_mágico(mágico), True)
    confere("Ex. 10 - não é quadrado mágico",
            é_quadrado_mágico([[1, 2], [3, 4]]), False)

    # Ex. 11
    permutação = [[0, 0, 1, 0, 0],
                  [0, 1, 0, 0, 0],
                  [0, 0, 0, 0, 1],
                  [1, 0, 0, 0, 0],
                  [0, 0, 0, 1, 0]]
    confere("Ex. 11 - é matriz de permutações",
            é_matriz_permutação(permutação), True)
    confere("Ex. 11 - não é matriz de permutações",
            é_matriz_permutação([[1, 1], [0, 0]]), False)


def menu():
    while True:
        print()
        print("=" * 50)
        print(" EXERCÍCIOS - MATRIZES")
        print("=" * 50)
        print(" 0  - Rodar todos os exercícios de uma vez")
        print(" 1  - Ler e mostrar uma matriz")
        print(" 2  - Dimensões de uma matriz")
        print(" 3  - Imprimir uma matriz")
        print(" 4  - Transposta")
        print(" 5  - Soma de duas matrizes")
        print(" 6  - Produto de duas matrizes")
        print(" 7  - É matriz diagonal?")
        print(" 8  - É triangular inferior?")
        print(" 9  - É triangular superior?")
        print(" 10 - É quadrado mágico?")
        print(" 11 - É matriz de permutações?")
        print(" s  - Sair")
        opção = input("Escolha: ").strip().lower()

        if opção == "s":
            print("Até mais!")
            break
        elif opção == "0":
            testa_todos_os_exemplos()
        elif opção == "1":
            M = lê_matriz_com_aviso()
            print("Matriz lida (como lista de listas):", M)
        elif opção == "2":
            M = lê_matriz_com_aviso()
            dim = dimensões(M)
            if dim == ():
                print("-> Não é uma matriz válida.")
            else:
                print(f"-> É uma matriz {dim[0]} x {dim[1]}.")
        elif opção == "3":
            M = lê_matriz_com_aviso()
            print("Matriz impressa:")
            imprime_matriz(M)
        elif opção == "4":
            M = lê_matriz_com_aviso()
            print("Transposta:")
            imprime_matriz(transposta(M))
        elif opção == "5":
            A = lê_matriz_com_aviso("a matriz A")
            B = lê_matriz_com_aviso("a matriz B")
            C = soma(A, B)
            if C == []:
                print("-> Dimensões incompatíveis (ou matriz inválida).")
            else:
                print("A + B =")
                imprime_matriz(C)
        elif opção == "6":
            A = lê_matriz_com_aviso("a matriz A")
            B = lê_matriz_com_aviso("a matriz B")
            C = produto(A, B)
            if C == []:
                print("-> Dimensões incompatíveis (ou matriz inválida).")
            else:
                print("A x B =")
                imprime_matriz(C)
        elif opção == "7":
            mostra_resultado_bool("uma matriz diagonal",
                                  é_diagonal(lê_matriz_com_aviso()))
        elif opção == "8":
            mostra_resultado_bool("uma matriz triangular inferior",
                                  é_triangular_inferior(lê_matriz_com_aviso()))
        elif opção == "9":
            mostra_resultado_bool("uma matriz triangular superior",
                                  é_triangular_superior(lê_matriz_com_aviso()))
        elif opção == "10":
            mostra_resultado_bool("um quadrado mágico",
                                  é_quadrado_mágico(lê_matriz_com_aviso()))
        elif opção == "11":
            mostra_resultado_bool("uma matriz de permutações",
                                  é_matriz_permutação(lê_matriz_com_aviso()))
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()