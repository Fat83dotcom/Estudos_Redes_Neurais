import numpy as np


entrada = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
saida = np.array([0, 0, 0, 1])
pesos = np.array([0.0, 0.0])
txAprendizagem = 0.1


def stepFunction(soma) -> int:
    return 1 if soma >= 1 else 0


def calcSaida(registro) -> int:
    return stepFunction(registro.dot(pesos))


def treinar() -> None:
    erroTotal = 1
    while erroTotal != 0:
        erroTotal = 0
        for i in range(len(saida)):
            saidaCalculada = calcSaida(np.asarray(entrada[i]))
            erro = abs(saida[i] - saidaCalculada)
            erroTotal += erro
            if erro != 0:
                for j in range(len(pesos)):
                    pesos[j] = pesos[j] + (
                        txAprendizagem * entrada[i][j] * erro
                    )
                    print(f'Peso atualizado: {pesos[j]}')
        print(f'Total de erros: {erroTotal}')


treinar()
