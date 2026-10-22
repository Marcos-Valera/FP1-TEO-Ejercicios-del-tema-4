import csv
from collections import namedtuple

Pelicula = namedtuple('Pelicula', [
    "fecha_estreno",   # tipo date
    "titulo",          # tipo str
    "director",        # tipo str
    "genero",          # tipo list[str]
    "duracion",        # tipo int
    "presupuesto",     # tipo int
    "recaudacion",     # tipo int
    "reparto"          # tipo list[str]
])

def lee_peliculas(ruta_fichero: str) -> list[Pelicula]:    
    with open(ruta_fichero, encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector) # Saltamos la cabecera
        for linea in lector:
            # TODO: Depura para observar qué hay en linea
            # TODO: Modifica el for para obtener cada campo en una variable mediante unpacking
            # TODO: Crea una tupla de tipo Pelicula para cada iteración del bucle, rellenándola con los datos adecuados
            pass
    

def existe_pelicula(peliculas: list[Pelicula], cadena_en_titulo: str) -> bool:
    """
    Comprueba si existe alguna película cuyo título contenga la cadena dada.
    Parámetros:
    peliculas (list[Pelicula]): Lista de películas.
    cadena_en_titulo (str): Cadena a buscar en los títulos de las películas.
    Devuelve:
    bool: True si existe al menos una película cuyo título contiene la cadena, False en caso
    contrario.
    """
    # TODO: Implementa esta función
    pass

def son_todas_director_genero(peliculas: list[Pelicula], director: str, genero: str) -> bool:
    """
    Comprueba si todas las películas del director dado pertenecen al género indicado.
    Parámetros:
    peliculas (list[Pelicula]): Lista de películas.
    director (str): Nombre del director.
    genero (str): Género a comprobar.
    Devuelve:
    bool: True si todas las películas del director pertenecen al género, False en caso contrario.
    """
    # TODO: Implementa esta función
    pass

def construye_lista_titulos_actor(peliculas: list[Pelicula], actor: str) -> list[str]:
    """
    Devuelve una lista de títulos en los que el actor indicado aparece en el reparto.
    Parámetros:
    peliculas (list[Pelicula]): Lista de películas.
    actor (str): Nombre del actor.
    Devuelve:
    list[str]: Lista de títulos de películas en las que aparece el actor.
    """    
    # TODO: Implementa esta función
    pass

def calcula_presupuesto_total_año(peliculas: list[Pelicula], año: int) -> int:
    """
    Suma y devuelve el presupuesto total de las películas cuyo año de estreno es el indicado.
    Parámetros:
    peliculas (list[Pelicula]): Lista de películas.
    año (int): Año de estreno.
    Devuelve:
    int: Presupuesto total de las películas estrenadas en el año indicado.
    """
    # TODO: Implementa esta función
    pass

def encuentra_pelicula_mayor_recaudacion(peliculas: list[Pelicula], genero: str) -> Pelicula | None:
    """
    Devuelve la película con mayor recaudacion entre las que incluyen el genero dado.
    Parámetros:
    peliculas (list[Pelicula]): Lista de películas.
    genero (str): Género a buscar.
    Devuelve:
    Pelicula | None: Película con mayor recaudación del género indicado, o None si no existe ninguna.
    """
    # TODO: Implementa esta función
    pass






