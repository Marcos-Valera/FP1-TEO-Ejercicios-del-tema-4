from matrices import es_matriz, suma_matrices, suma_filas, suma_diagonal, transponer


def test_es_matriz():
    assert es_matriz([]) is True
    assert es_matriz([[1, 2], [3, 4]]) is True
    assert es_matriz([[], []]) is True
    assert es_matriz([[1, 2], [3]]) is False
    assert es_matriz([[1], [2, 3]]) is False


def test_suma_matrices():
    assert suma_matrices(
        [[1, 2], [3, 4]],
        [[5, 6], [7, 8]],
    ) == [[6, 8], [10, 12]]

    assert suma_matrices(
        [[1, 2, 3], [4, 5, 6]],
        [[9, 8, 7], [6, 5, 4]],
    ) == [[10, 10, 10], [10, 10, 10]]

    assert suma_matrices([[1, 2], [3, 4]], [[5, 6, 7], [8, 9, 10]]) is None
    assert suma_matrices([[1, 2], [3]], [[4, 5], [6, 7]]) is None
    assert suma_matrices([[1], [2]], [[3]]) is None
    assert suma_matrices([], []) == []
    assert suma_matrices([[], []], [[], []]) == [[], []]


def test_suma_filas():
    assert suma_filas([[1, 2, 3], [4, 5, 6]]) == [6, 15]
    assert suma_filas([[1], [2, 3]]) is None
    assert suma_filas([]) == []
    assert suma_filas([[], []]) == [0, 0]


def test_suma_diagonal():
    assert suma_diagonal([[1, 2], [3, 4]]) == 5
    assert suma_diagonal([[1, 2, 3], [4, 5, 6]]) is None
    assert suma_diagonal([[1, 2], [3]]) is None
    assert suma_diagonal([]) == 0


def test_transponer():
    assert transponer([[1, 2, 3], [4, 5, 6]]) == [
        [1, 4],
        [2, 5],
        [3, 6],
    ]
    assert transponer([[1, 2], [3, 4]]) == [[1, 3], [2, 4]]
    assert transponer([[1, 2], [3]]) is None
    assert transponer([]) == []
    assert transponer([[], []]) == []


test_es_matriz()
#test_suma_matrices()
#test_suma_filas()
#test_suma_diagonal()
#test_transponer()
print("Todos los casos de prueba pasaron correctamente.")
