def es_matriz(matriz: list[list[int | float]]) -> bool:
    """
    Comprueba si una lista de listas representa una matriz válida.

    Parámetros:
    matriz (list[list[int | float]]): Lista de listas que se quiere comprobar.

    Devuelve:
    bool: True si todas las filas tienen el mismo número de elementos.
    """

    # Si la matriz está vacía, es una matriz válida
    if len(matriz) == 0:
        return True

    n_columnas = len(matriz[0]) # Encontramos el número de columnas de la primera fila

    # Si alguna fila no tiene el mismo número de columnas, devolvemos False, sino, True
    for fila in matriz[1:]:
        if len(fila) != n_columnas:
            return False
    return True
        



def suma_matrices(
    m1: list[list[int | float]], m2: list[list[int | float]]
) -> list[list[int | float]] | None:
    """
    Suma dos matrices de las mismas dimensiones.

    Parámetros:
    m1 (list[list[int | float]]): Primera matriz.
    m2 (list[list[int | float]]): Segunda matriz.

    Devuelve:
    list[list[int | float]] | None: Matriz resultante, o None si las matrices
    no son válidas o tienen dimensiones distintas.
    """
    # Si no son matrices, devolvemos None
    if not es_matriz(m1) or not es_matriz(m2):
        return None

    # Comprobamos que tengan el mismo número de filas
    if len(m1) != len(m2):
        return None

    # Si ambas matrices están vacías, se permite la suma y el resultado es la matriz vacía
    if len(m1) == 0:
        return []

    # Comprobamos que tengan el mismo número de columnas
    if len(m1[0]) != len(m2[0]):
        return None

    matriz_suma = [] # Inicializamos la suma vacía
    for fila1, fila2 in zip(m1, m2): # Cada fila, en paralelo
        fila_suma = [] # Reiniciamos la fila suma para cada iteración
        for celda1, celda2 in zip(fila1, fila2): # Cada celda, en paralelo
            suma = celda1 + celda2
            fila_suma.append(suma) # Añadimos la celda sumada a la fila
        matriz_suma.append(fila_suma) # Añadimos la fila sumada a la matriz como nueva fila

    return matriz_suma


def suma_filas(
    matriz: list[list[int | float]],
) -> list[int | float] | None:
    """
    Suma los elementos de cada fila de una matriz.

    Parámetros:
    matriz (list[list[int | float]]): Matriz cuyos elementos se sumarán.

    Devuelve:
    list[int | float] | None: Lista con la suma de cada fila, o None si la
    matriz no es válida.
    """
    if not es_matriz(matriz):
        return None

    fila_suma = []
    for fila in matriz:
        suma_fila = sum(fila)
        fila_suma.append(suma_fila)

    return fila_suma


def suma_diagonal(matriz: list[list[int | float]]) -> int | float | None:
    """
    Suma los elementos de la diagonal principal de una matriz cuadrada.

    Parámetros:
    matriz (list[list[int | float]]): Matriz cuadrada de números.

    Devuelve:
    int | float | None: Suma de la diagonal, o None si la matriz no es válida
    o no es cuadrada.
    """
     # Si no es matriz, devolvemos None
    if not es_matriz(matriz):
        return None

    # Si la matriz está vacía, la suma de la diagonal principal es 0
    if len(matriz) == 0:
        return 0

    # Comprobamos que tenga el mismo número de filas que de columnas
    if len(matriz) != len(matriz[0]):
        return None

    suma_diagonal = 0
    for i in range(len(matriz)):
        suma_diagonal += matriz[i][i]
    return suma_diagonal


def transponer(
    matriz: list[list[int | float]],
) -> list[list[int | float]] | None:
    """
    Devuelve la matriz transpuesta.

    Parámetros:
    matriz (list[list[int | float]]): Matriz que se quiere transponer.

    Devuelve:
    list[list[int | float]] | None: Matriz transpuesta, o None si la matriz
    no es válida.
    """

    if not es_matriz(matriz):
        return None

    if len(matriz) == 0:
        return []

    matriz_traspuesta = []
    for i in range(len(matriz[0])):
        nueva_fila = []
        for fila in matriz:
            nueva_fila.append(fila[i])
        matriz_traspuesta.append(nueva_fila)

    return matriz_traspuesta