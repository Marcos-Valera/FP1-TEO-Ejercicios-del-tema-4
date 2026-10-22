# FP1 - Teoría - Ejercicios del Tema 4

## Ejercicio 1: Generador de listas aleatorias sin repeticiones consecutivas

Implementa una función `genera_aleatorios` que genere una lista de números enteros aleatorios, sin que haya dos elementos consecutivos que sean iguales.  La función permite indicar mediante parámetros el rango en el que se generan los números aleatorios, y el tamaño de la lista a generar.

Prueba la implementación ejecutando las pruebas del módulo `listas_test.py`.

## Ejercicio 2: Intercala listas

Implementa una función `intercala_listas` que reciba dos listas y devuelva una nueva lista intercalando los elementos de las listas recibidas: primero un elemento de la primera, luego un elemento de la segunda, luego un elemento de la primera, etc. Si una de las listas tiene más elementos que la otra, se introducirán todos los elementos sobrantes tal cual en la lista resultante.

Prueba la implementación ejecutando las pruebas del módulo `listas_test.py`.

## Ejercicio 3: Mezcla listas ordenadas

Implementa una función `mezcla_ordenadas` que reciba dos listas ordenadas y devuelva una nueva lista también ordenada con todos los elementos de ambas listas. Si una de las listas tiene más elementos que la otra, se introducirán todos los elementos sobrantes tal cual en la lista resultante.

Prueba la implementación ejecutando las pruebas del módulo `listas_test.py`.

## Ejercicio 4: Ordenación *Bubble Sort*

El método de ordenación *Bubble Sort* no es el método más eficiente para ordenar una lista, pero es relativamente sencillo de implementar. El algoritmo es el siguiente:

1. Recorre la lista comparando elementos adyacentes.
2. Si un par de elementos está en el orden incorrecto, se intercambian.
3. Se repite el proceso hasta que no se realicen más intercambios en una pasada completa.

Prueba la implementación ejecutando las pruebas del módulo `listas_test.py`.

## Ejercicio 5: Datos de películas

Disponemos de datos sobre películas en un fichero con formato CSV (*Comma-Separated Values*), ubicado en `data/peliculas.csv`. Python dispone de un módulo `csv` con utilidades para leer este tipo de archivos. Queremos implementar una serie de funciones en el módulo `peliculas.py` para leer los datos del fichero y contestar a ciertas preguntas sobre las películas. Cada película estará representada por una tupla nombrada `Pelicula`, que ya está definida en `peliculas.py`.

### Función `lee_peliculas`

Se te proporciona parte de la implementación de `lee_peliculas`:
* Ejecuta con ayuda del depurador una llamada a esta función, y observa cómo funciona la lectura del CSV.
* Modifica el `for` para que use una variable por cada campo del CSV mediante *unpacking*.
* Implementa el código dentro del `for` para que se construya una tupla de tipo `Pelicula` con los valores de las variables del `for`. Asegúrate de que cada valor sea del tipo adecuado
* La función debe acumular todas las tuplas creadas en una lista, y finalmente devolverla.

Una vez que lo tengas implementado, ejecuta las pruebas que se te proporcionan en el módulo `peliculas_test.py`.

### Función `existe_pelicula`

Devuelve `True` si existe alguna película cuyo titulo contiene una determinada cadena, y `False` en caso contrario. Una vez que lo tengas implementado, ejecuta las pruebas que se te proporcionan en el módulo `peliculas_test.py`.

### Función `son_todas_director_genero`

Devuelve `True` si todas las películas de un director dado contienen el genero indicado en su lista de géneros, y `False` en caso contrario. Una vez que lo tengas implementado, ejecuta las pruebas que se te proporcionan en el módulo `peliculas_test.py`.

### Función `construye_lista_titulos_actor`

Devuelve una lista de títulos en los que el actor indicado aparece en el reparto. Una vez que lo tengas implementado, ejecuta las pruebas que se te proporcionan en el módulo `peliculas_test.py`.

### Función `calcula_presupuesto_total_año`

Suma y devuelve el presupuesto total de las películas cuyo año de estreno es el indicado. Una vez que lo tengas implementado, ejecuta las pruebas que se te proporcionan en el módulo `peliculas_test.py`.

### Función `encuentra_pelicula_mayor_recaudacion`

Devuelve la película con mayor recaudacion entre las que incluyen el genero dado. Si no existe ninguna de ese género, devuelve `None`. Una vez que lo tengas implementado, ejecuta las pruebas que se te proporcionan en el módulo `peliculas_test.py`.

## Ejercicio 6: Comprobar si una lista de listas es una matriz válida

Implementa una función `es_matriz` en el módulo `matrices.py` que reciba una lista de listas de números y devuelva `True` si representa una matriz válida, y `False` en caso contrario. Para este ejercicio, una matriz es válida si todas sus filas tienen el mismo número de elementos. Considera que una lista vacía representa una matriz válida (la matriz vacía).

Esta función se utilizará en los ejercicios siguientes para comprobar que las matrices recibidas son válidas.

## Ejercicio 7: Suma de matrices

Implementa una función `suma_matrices` en el módulo `matrices.py` que reciba dos matrices numéricas de las mismas dimensiones y devuelva el resultado de sumar ambas.

Antes de llevar a cabo el algoritmo de suma, utiliza `es_matriz` para comprobar que ambas matrices son válidas. Comprueba también que ambas matrices tienen el mismo número de filas y y el mismo número de columnas. Si no se cumple alguna de estas condiciones, la función debe devolver `None`.

Ejecuta las pruebas del módulo `matrices_test.py` y asegúrate de que se pasan todas correctamente.

## Ejercicio 8: Sumar los elementos de cada fila

Implementa una función `suma_filas` en el módulo `matrices.py` que reciba una matriz válida de números y devuelva una lista con la suma de los elementos de cada fila.

Por ejemplo, para la matriz `[[1, 2, 3], [4, 5, 6]]`, la función devolverá `[6, 15]`. Utiliza la función `es_matriz` para comprobar la matriz. Si no es válida, devuelve `None`.

## Ejercicio 9: Sumar la diagonal principal

Implementa una función `suma_diagonal` en el módulo `matrices.py` que reciba una matriz **cuadrada** de números y devuelva la suma de los elementos de su diagonal principal.

Antes de calcular la suma, utiliza `es_matriz` para comprobar que la matriz sea válida, y asegúrate de que tenga el mismo número de filas que de columnas (matriz cuadrada). Si no se cumple alguna de estas condiciones, devuelve `None`.

## Ejercicio 10: Transponer una matriz

Implementa una función `transponer` en el módulo `matrices.py` que reciba una matriz válida y devuelva una nueva matriz transpuesta: las filas de la matriz original pasarán a ser columnas, y sus columnas pasarán a ser filas. Utiliza `es_matriz` para comprobar la matriz. Si no es válida, devuelve `None`.

Para construir la matriz transpuesta, sigue estos pasos:

1. Si la matriz no tiene filas, devuelve una matriz vacía.
2. Crea una lista vacía para guardar el resultado.
3. Recorre los índices de las columnas de la matriz original.
4. Para cada índice de columna, crea una nueva fila vacía.
5. Recorre las filas de la matriz original y añade a la nueva fila el elemento que está en la columna actual.
6. Añade la nueva fila al resultado.
7. Devuelve el resultado.

Por ejemplo, `[[1, 2, 3], [4, 5, 6]]` se transpone a `[[1, 4], [2, 5], [3, 6]]`.

## Ejercicio 11: Lista de nombres ordenada por longitud

Queremos trabajar con listas de nombres que se mantengan siempre ordenadas por longitud de los nombres. Para ello, implementa una función `inserta_ordenado` en el módulo `listas.py` que reciba una lista y un nuevo nombre y lo inserte en la posición adecuada. Supondremos que la lista recibida está previamente ordenada según el criterio especificado.

Antes de llevar a cabo el algoritmo de inserción en orden, la función comprobará que la lista recibida esté correctamente ordenada. Si no lo estuviera, la función no hará nada (la lista recibida no es modificada).

Prueba la implementación ejecutando las pruebas del módulo `listas_test.py`.

## Ejercicio 12: Buscar duplicados

Implementa una función `busca_duplicados` en el módulo `listas.py` que reciba una lista y devuelva otra lista con los elementos de la primera que aparecen más de una vez. Dichos elementos deben aparecer en la lista devuelta en el mismo orden en que estaban en la lista recibida.

Por ejemplo, para la entrada `[1, 2, 3, 2, 4, 3, 5]`, la función devolverá `[2, 3]`: cada elemento duplicado aparece una sola vez en el resultado, respetando el orden de su primera aparición.

Intenta implementarlo de dos formas:
1. Usando el método `count`:

    Recorre los elementos de la lista y utiliza `count` para comprobar cuántas veces aparece cada uno. Si aparece más de una vez, añádelo a la lista resultado (solo si todavía no está en ella).
2. Usando *slicing* y sin usar el método `count`:

    Recorre la lista con sus índices y compara cada elemento con el trozo de lista que queda a continuación. Si vuelve a aparecer en ese trozo, añádelo a la lista resultado (solo si todavía no está en ella).


Prueba la implementación ejecutando las pruebas del módulo `listas_test.py`.
