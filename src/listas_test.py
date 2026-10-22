from listas import genera_aleatorios, intercala_listas, mezcla_ordenadas, ordena_bubble_sort, inserta_ordenado, busca_duplicados

def test_genera_aleatorios():
    # Caso de prueba 1: Generar 50 números entre 1 y 5
    n = 50
    minimo = 1
    maximo = 5
    resultado = genera_aleatorios(n, minimo, maximo)
    assert len(resultado) == n
    for n1, n2 in zip(resultado, resultado[1:]):
        assert n1 != n2

    # Caso de prueba 2: Generar 0 números
    n = 0
    minimo = 1
    maximo = 10
    resultado = genera_aleatorios(n, minimo, maximo)
    assert resultado == []

def test_intercala_listas():
    # Caso de prueba 1: Listas de igual longitud
    lista1 = [1, 3, 5]
    lista2 = [2, 4, 6]
    resultado_esperado = [1, 2, 3, 4, 5, 6]
    assert intercala_listas(lista1, lista2) == resultado_esperado

    # Caso de prueba 2: Lista1 más larga que Lista2
    lista1 = [1, 3, 5, 7]
    lista2 = [2, 4]
    resultado_esperado = [1, 2, 3, 4, 5, 7]
    assert intercala_listas(lista1, lista2) == resultado_esperado

    # Caso de prueba 3: Lista2 más larga que Lista1
    lista1 = [1, 3]
    lista2 = [2, 4, 6, 8]
    resultado_esperado = [1, 2, 3, 4, 6, 8]
    assert intercala_listas(lista1, lista2) == resultado_esperado

    # Caso de prueba 4: Una lista vacía
    lista1 = []
    lista2 = [2, 4, 6]
    resultado_esperado = [2, 4, 6]
    assert intercala_listas(lista1, lista2) == resultado_esperado

    # Caso de prueba 5: Ambas listas vacías
    lista1 = []
    lista2 = []
    resultado_esperado = []
    assert intercala_listas(lista1, lista2) == resultado_esperado

def test_mezcla_ordenadas():
    # Caso de prueba 1: Listas de igual longitud
    lista1 = [1, 3, 5]
    lista2 = [2, 4, 6]
    resultado_esperado = [1, 2, 3, 4, 5, 6]
    assert mezcla_ordenadas(lista1, lista2) == resultado_esperado

    # Caso de prueba 2: Lista1 más larga que Lista2
    lista1 = [1, 3, 5, 7]
    lista2 = [2, 4]
    resultado_esperado = [1, 2, 3, 4, 5, 7]
    assert mezcla_ordenadas(lista1, lista2) == resultado_esperado

    # Caso de prueba 3: Lista2 más larga que Lista1
    lista1 = [1, 3]
    lista2 = [2, 4, 6, 8]
    resultado_esperado = [1, 2, 3, 4, 6, 8]
    assert mezcla_ordenadas(lista1, lista2) == resultado_esperado

    # Caso de prueba 4: Una lista vacía
    lista1 = []
    lista2 = [2, 4, 6]
    resultado_esperado = [2, 4, 6]
    assert mezcla_ordenadas(lista1, lista2) == resultado_esperado

    # Caso de prueba 5: Ambas listas vacías
    lista1 = []
    lista2 = []
    resultado_esperado = []
    assert mezcla_ordenadas(lista1, lista2) == resultado_esperado

def test_ordena_bubble_sort():
    # Caso de prueba 1: Lista desordenada
    lista = [5, 3, 8, 1, 2]
    resultado_esperado = [1, 2, 3, 5, 8]
    ordena_bubble_sort(lista)
    assert lista == resultado_esperado

    # Caso de prueba 2: Lista ya ordenada
    lista = [1, 2, 3, 4, 5]
    resultado_esperado = [1, 2, 3, 4, 5]
    ordena_bubble_sort(lista)
    assert lista == resultado_esperado

    # Caso de prueba 3: Lista con elementos iguales
    lista = [4, 4, 4, 4]
    resultado_esperado = [4, 4, 4, 4]
    ordena_bubble_sort(lista)
    assert lista == resultado_esperado

    # Caso de prueba 4: Lista vacía
    lista = []
    resultado_esperado = []
    ordena_bubble_sort(lista)
    assert lista == resultado_esperado

    # Caso de prueba 5: Lista con un solo elemento
    lista = [42]
    resultado_esperado = [42]
    ordena_bubble_sort(lista)
    assert lista == resultado_esperado

def test_inserta_ordenado():
    # Caso de prueba 1: Inserción en una lista vacía
    lista = []
    inserta_ordenado(lista, "Ana")
    assert lista == ["Ana"]

    # Caso de prueba 2: Inserción al principio
    lista = ["Juan", "Pedro", "Sofía"]
    inserta_ordenado(lista, "Al")
    assert lista == ["Al", "Juan", "Pedro", "Sofía"]

    # Caso de prueba 3: Inserción en el medio
    lista = ["Ana", "María", "Carlos"]
    inserta_ordenado(lista, "Luis")
    assert lista == ["Ana", "Luis", "María", "Carlos"]

    # Caso de prueba 4: Inserción al final
    lista = ["Eva", "Lina", "Roberto"]
    inserta_ordenado(lista, "Sebastián")
    assert lista == ["Eva", "Lina", "Roberto", "Sebastián"]

    # Caso de prueba 5: Lista no ordenada
    lista = ["Pedro", "Ana", "Sofía"]
    inserta_ordenado(lista, "Luis")
    assert lista == ["Pedro", "Ana", "Sofía"]  # La lista no cambia

def test_busca_duplicados():
    # Caso de prueba 1: Lista con duplicados
    lista = [1, 2, 3, 2, 4, 3, 5]
    resultado_esperado = [2, 3]
    assert busca_duplicados(lista) == resultado_esperado

    # Caso de prueba 2: Lista sin duplicados
    lista = [1, 2, 3, 4, 5]
    resultado_esperado = []
    assert busca_duplicados(lista) == resultado_esperado

    # Caso de prueba 3: Lista con todos los elementos duplicados
    lista = [1, 1, 1, 1]
    resultado_esperado = [1]
    assert busca_duplicados(lista) == resultado_esperado

    # Caso de prueba 4: Lista vacía
    lista = []
    resultado_esperado = []
    assert busca_duplicados(lista) == resultado_esperado

    # Caso de prueba 5: Lista con elementos de diferentes tipos
    lista = [1, "a", 2, "b", "a", 1]
    resultado_esperado = [1, "a"]
    assert busca_duplicados(lista) == resultado_esperado

# Descomenta las llamadas de los tests que quieras ejecutar
test_genera_aleatorios()
#test_intercala_listas()
#test_mezcla_ordenadas()
#test_ordena_bubble_sort()
#test_inserta_ordenado()
#test_busca_duplicados()
print("Todos los casos de prueba pasaron correctamente.")