def dentro_do_tabuleiro(linha, coluna):
    return 0 <= linha < 8 and 0 <= coluna < 8


def cor_da_peca(peca):
    if peca is None:
        return None
    return peca[0]


def movimento_cavalo(tabuleiro, linha_origem, coluna_origem, linha_destino, coluna_destino):
    if not dentro_do_tabuleiro(linha_origem, coluna_origem):
        return False
    if not dentro_do_tabuleiro(linha_destino, coluna_destino):
        return False
    if (linha_origem, coluna_origem) == (linha_destino, coluna_destino):
        return False

    peca = tabuleiro[linha_origem][coluna_origem]
    if peca is None or peca[1] != 'N':
        return False

    destino = tabuleiro[linha_destino][coluna_destino]
    cor = cor_da_peca(peca)
    if destino is not None and cor_da_peca(destino) == cor:
        return False

    delta_linha = abs(linha_destino - linha_origem)
    delta_coluna = abs(coluna_destino - coluna_origem)

    return (delta_linha == 2 and delta_coluna == 1) or (delta_linha == 1 and delta_coluna == 2)


def testar_movimentos():
    tabuleiro = [[None for _ in range(8)] for _ in range(8)]
    tabuleiro[7][4] = 'wN'

    print(movimento_cavalo(tabuleiro, 7, 4, 5, 3))
    print(movimento_cavalo(tabuleiro, 7, 4, 6, 2))
    print(movimento_cavalo(tabuleiro, 7, 4, 7, 5))

    tabuleiro[5][3] = 'bP'
    print(movimento_cavalo(tabuleiro, 7, 4, 5, 3))


if __name__ == "__main__":
    testar_movimentos()