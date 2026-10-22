from peliculas import *
import datetime

# Datos de prueba para los tests
PELICULAS_CSV = [
    Pelicula(fecha_estreno=datetime.date(2019, 12, 19), titulo='Star Wars: The Rise of Skywalker', director='J.J. Abrams', genero=['Acción', 'Aventura', 'Fantasía'], duracion=142, presupuesto=275, recaudacion=1074, reparto=['Daisy Ridley', 'Adam Driver', 'John Boyega']), 
    Pelicula(fecha_estreno=datetime.date(2019, 5, 23), titulo='Joker', director='Todd Phillips', genero=['Drama'], duracion=122, presupuesto=55, recaudacion=980, reparto=['Joaquin Phoenix', 'Robert De Niro', 'Zazie Beetz']), 
    Pelicula(fecha_estreno=datetime.date(2019, 11, 22), titulo='Frozen II', director='Chris Buck', genero=['Animación', 'Aventura', 'Comedia'], duracion=103, presupuesto=150, recaudacion=1450, reparto=['Idina Menzel', 'Kristen Bell', 'Jonathan Groff']), 
    Pelicula(fecha_estreno=datetime.date(2020, 2, 14), titulo='Parasite', director='Bong Joon-ho', genero=['Drama', 'Thriller'], duracion=132, presupuesto=11, recaudacion=254, reparto=['Song Kang-ho', 'Lee Sun-kyun', 'Cho Yeo-jeong']), 
    Pelicula(fecha_estreno=datetime.date(2018, 11, 9), titulo='Bohemian Rhapsody', director='Bryan Singer', genero=['Drama', 'Musical'], duracion=134, presupuesto=52, recaudacion=903, reparto=['Rami Malek', 'Lucy Boynton', 'Gwilym Lee']), 
    Pelicula(fecha_estreno=datetime.date(2019, 5, 2), titulo='Avengers: Endgame', director='Anthony Russo', genero=['Acción', 'Aventura', 'Fantasía'], duracion=181, presupuesto=356, recaudacion=2798, reparto=['Robert Downey Jr.', 'Chris Evans', 'Mark Ruffalo']), 
    Pelicula(fecha_estreno=datetime.date(2018, 12, 14), titulo='Spider-Man: Into the Spider-Verse', director='Bob Persichetti', genero=['Animación', 'Acción', 'Aventura'], duracion=117, presupuesto=90, recaudacion=375, reparto=['Shameik Moore', 'Jake Johnson', 'Hailee Steinfeld']), 
    Pelicula(fecha_estreno=datetime.date(2017, 11, 9), titulo='Justice League', director='Zack Snyder', genero=['Acción', 'Aventura', 'Fantasía'], duracion=121, presupuesto=300, recaudacion=657, reparto=['Ben Affleck', 'Gal Gadot', 'Jason Momoa']), 
    Pelicula(fecha_estreno=datetime.date(2016, 11, 3), titulo='Doctor Strange', director='Scott Derrickson', genero=['Acción', 'Aventura', 'Fantasía'], duracion=115, presupuesto=165, recaudacion=678, reparto=['Benedict Cumberbatch', 'Chiwetel Ejiofor', 'Rachel McAdams']), 
    Pelicula(fecha_estreno=datetime.date(2015, 7, 24), titulo='Ant-Man', director='Peyton Reed', genero=['Acción', 'Aventura', 'Comedia'], duracion=117, presupuesto=130, recaudacion=519, reparto=['Paul Rudd', 'Michael Douglas', 'Evangeline Lilly']), 
    Pelicula(fecha_estreno=datetime.date(2014, 12, 19), titulo='The Hobbit: The Battle of the Five Armies', director='Peter Jackson', genero=['Acción', 'Aventura', 'Fantasía'], duracion=144, presupuesto=250, recaudacion=956, reparto=['Martin Freeman', 'Ian McKellen', 'Richard Armitage']), 
    Pelicula(fecha_estreno=datetime.date(2013, 12, 20), titulo='The Wolf of Wall Street', director='Martin Scorsese', genero=['Drama', 'Comedia'], duracion=180, presupuesto=100, recaudacion=392, reparto=['Leonardo DiCaprio', 'Jonah Hill', 'Margot Robbie']), 
    Pelicula(fecha_estreno=datetime.date(2012, 11, 22), titulo='Skyfall', director='Sam Mendes', genero=['Acción', 'Aventura', 'Thriller'], duracion=143, presupuesto=200, recaudacion=1108, reparto=['Daniel Craig', 'Judi Dench', 'Javier Bardem']), 
    Pelicula(fecha_estreno=datetime.date(2011, 11, 18), titulo='The Twilight Saga: Breaking Dawn – Part 1', director='Bill Condon', genero=['Drama', 'Fantasía', 'Romance'], duracion=117, presupuesto=110, recaudacion=709, reparto=['Kristen Stewart', 'Robert Pattinson', 'Taylor Lautner']), 
    Pelicula(fecha_estreno=datetime.date(2010, 7, 9), titulo='Inception', director='Christopher Nolan', genero=['Acción', 'Aventura', 'Thriller'], duracion=148, presupuesto=160, recaudacion=829, reparto=['Leonardo DiCaprio', 'Ken Watanabe', 'Joseph Gordon-Levitt']), 
    Pelicula(fecha_estreno=datetime.date(2009, 5, 22), titulo='Up', director='Pete Docter', genero=['Animación', 'Aventura', 'Comedia'], duracion=96, presupuesto=175, recaudacion=731, reparto=['Edward Asner', 'Jordan Nagai', 'John Ratzenberger']), 
    Pelicula(fecha_estreno=datetime.date(2008, 12, 25), titulo='The Dark Knight', director='Christopher Nolan', genero=['Acción', 'Aventura', 'Crimen'], duracion=152, presupuesto=185, recaudacion=1004, reparto=['Christian Bale', 'Heath Ledger', 'Aaron Eckhart']), 
    Pelicula(fecha_estreno=datetime.date(2008, 5, 3), titulo='Iron Man', director='Jon Favreau', genero=['Acción', 'Aventura', 'Ciencia ficción'], duracion=126, presupuesto=140, recaudacion=585, reparto=['Robert Downey Jr.', 'Terrence Howard', 'Jeff Bridges']), 
    Pelicula(fecha_estreno=datetime.date(2007, 12, 19), titulo='I am Legend', director='Francis Lawrence', genero=['Drama', 'Ciencia ficción', 'Thriller'], duracion=101, presupuesto=150, recaudacion=585, reparto=['Will Smith', 'Alice Braga', 'Charlie Tahan']), 
    Pelicula(fecha_estreno=datetime.date(2006, 11, 3), titulo='The Prestige', director='Christopher Nolan', genero=['Drama', 'Misterio', 'Thriller'], duracion=130, presupuesto=40, recaudacion=109, reparto=['Hugh Jackman', 'Christian Bale', 'Michael Caine']), 
    Pelicula(fecha_estreno=datetime.date(2005, 11, 18), titulo='Harry Potter and the Goblet of Fire', director='Mike Newell', genero=['Aventura', 'Fantasía'], duracion=157, presupuesto=150, recaudacion=897, reparto=['Daniel Radcliffe', 'Emma Watson', 'Rupert Grint']), 
    Pelicula(fecha_estreno=datetime.date(2004, 5, 21), titulo='Shrek 2', director='Andrew Adamson', genero=['Animación', 'Aventura', 'Comedia'], duracion=93, presupuesto=150, recaudacion=919, reparto=['Mike Myers', 'Eddie Murphy', 'Cameron Diaz']), 
    Pelicula(fecha_estreno=datetime.date(2003, 12, 25), titulo='The Lord of the Rings: The Return of the King', director='Peter Jackson', genero=['Aventura', 'Fantasía'], duracion=201, presupuesto=94, recaudacion=1142, reparto=['Elijah Wood', 'Ian McKellen', 'Viggo Mortensen']), 
    Pelicula(fecha_estreno=datetime.date(2002, 11, 14), titulo='The Bourne Identity', director='Doug Liman', genero=['Acción', 'Aventura', 'Thriller'], duracion=119, presupuesto=60, recaudacion=214, reparto=['Matt Damon', 'Franka Potente', 'Chris Cooper']), 
    Pelicula(fecha_estreno=datetime.date(2001, 7, 18), titulo='Jurassic Park III', director='Joe Johnston', genero=['Acción', 'Aventura', 'Ciencia ficción'], duracion=92, presupuesto=93, recaudacion=361, reparto=['Sam Neill', 'William H. Macy', 'Téa Leoni']), 
    Pelicula(fecha_estreno=datetime.date(2017, 12, 15), titulo='Star Wars: The Last Jedi', director='Rian Johnson', genero=['Acción', 'Aventura', 'Fantasía'], duracion=152, presupuesto=200, recaudacion=1333, reparto=['Mark Hamill', 'Carrie Fisher', 'Adam Driver']), 
    Pelicula(fecha_estreno=datetime.date(2015, 8, 14), titulo='Furious 7', director='James Wan', genero=['Acción', 'Aventura', 'Crimen'], duracion=137, presupuesto=190, recaudacion=1516, reparto=['Vin Diesel', 'Paul Walker', 'Dwayne Johnson']), 
    Pelicula(fecha_estreno=datetime.date(2014, 11, 7), titulo='Interstellar', director='Christopher Nolan', genero=['Drama', 'Aventura', 'Ciencia ficción'], duracion=169, presupuesto=165, recaudacion=677, reparto=['Matthew McConaughey', 'Anne Hathaway', 'Jessica Chastain']), 
    Pelicula(fecha_estreno=datetime.date(2013, 7, 12), titulo='Despicable Me 2', director='Pierre Coffin', genero=['Animación', 'Comedia', 'Familia'], duracion=98, presupuesto=76, recaudacion=970, reparto=['Steve Carell', 'Kristen Wiig', 'Benjamin Bratt']), 
    Pelicula(fecha_estreno=datetime.date(2012, 7, 8), titulo='The Dark Knight Rises', director='Christopher Nolan', genero=['Acción', 'Aventura', 'Crimen'], duracion=164, presupuesto=250, recaudacion=1081, reparto=['Christian Bale', 'Tom Hardy', 'Anne Hathaway']), 
    Pelicula(fecha_estreno=datetime.date(2011, 5, 27), titulo='Pirates of the Caribbean: On Stranger Tides', director='Rob Marshall', genero=['Aventura', 'Fantasía'], duracion=136, presupuesto=410, recaudacion=1045, reparto=['Johnny Depp', 'Penélope Cruz', 'Ian McShane']), 
    Pelicula(fecha_estreno=datetime.date(2010, 6, 24), titulo='Toy Story 3', director='Lee Unkrich', genero=['Animación', 'Aventura', 'Comedia'], duracion=103, presupuesto=200, recaudacion=1063, reparto=['Tom Hanks', 'Tim Allen', 'Joan Cusack']), 
    Pelicula(fecha_estreno=datetime.date(2010, 5, 19), titulo='Iron Man 2', director='Jon Favreau', genero=['Acción', 'Aventura', 'Ciencia ficción'], duracion=124, presupuesto=200, recaudacion=623, reparto=['Robert Downey Jr.', 'Gwyneth Paltrow', 'Don Cheadle']), 
    Pelicula(fecha_estreno=datetime.date(2009, 12, 18), titulo='Avatar', director='James Cameron', genero=['Acción', 'Aventura', 'Fantasía'], duracion=162, presupuesto=237, recaudacion=2789, reparto=['Sam Worthington', 'Zoe Saldana', 'Sigourney Weaver']), 
    Pelicula(fecha_estreno=datetime.date(2008, 11, 28), titulo='Twilight', director='Catherine Hardwicke', genero=['Drama', 'Fantasía', 'Romance'], duracion=122, presupuesto=37, recaudacion=392, reparto=['Kristen Stewart', 'Robert Pattinson', 'Billy Burke']), 
    Pelicula(fecha_estreno=datetime.date(2002, 5, 2), titulo='Spider-Man', director='Sam Raimi', genero=['Acción', 'Aventura', 'Fantasía'], duracion=121, presupuesto=139, recaudacion=820, reparto=['Tobey Maguire', 'Willem Dafoe', 'Kirsten Dunst'])
]


def test_lee_peliculas():
    peliculas = lee_peliculas('data/peliculas.csv')    
    assert peliculas == PELICULAS_CSV

def test_existe_pelicula():
    peliculas = PELICULAS_CSV.copy()
    assert existe_pelicula(peliculas, "Inception") == True
    assert existe_pelicula(peliculas, "The Matrix") == False
    assert existe_pelicula(peliculas, "Star Wars") == True
    assert existe_pelicula(peliculas, "Avatar") == True
    assert existe_pelicula(peliculas, "no existe") == False

def test_todas_peliculas_director_genero():
    peliculas = PELICULAS_CSV.copy()
    assert son_todas_director_genero(peliculas, "Christopher Nolan", "Acción") == False
    assert son_todas_director_genero(peliculas, "Christopher Nolan", "Drama") == False
    assert son_todas_director_genero(peliculas, "J.J. Abrams", "Fantasía") == True
    assert son_todas_director_genero(peliculas, "Peter Jackson", "Aventura") == True

def test_construye_lista_titulos_actor():
    peliculas = PELICULAS_CSV.copy()
    lista_esperada_1 = [
        'The Dark Knight',
        'The Dark Knight Rises',
        'The Prestige'
    ]
    lista_esperada_2 = [
        'Star Wars: The Last Jedi'
    ]
    lista_esperada_3 = ['Inception', 'The Wolf of Wall Street']
    lista_esperada_4 = []
    assert sorted(construye_lista_titulos_actor(peliculas, "Christian Bale")) == sorted(lista_esperada_1)
    assert sorted(construye_lista_titulos_actor(peliculas, "Mark Hamill")) == sorted(lista_esperada_2)
    assert sorted(construye_lista_titulos_actor(peliculas, "Leonardo DiCaprio")) == sorted(lista_esperada_3)
    assert construye_lista_titulos_actor(peliculas, "Actor No Existente") == lista_esperada_4

def test_calcula_presupuesto_total_año():
    peliculas = PELICULAS_CSV.copy()
    assert calcula_presupuesto_total_año(peliculas, 2019) == 836
    assert calcula_presupuesto_total_año(peliculas, 2018) == 142
    assert calcula_presupuesto_total_año(peliculas, 2015) == 320
    assert calcula_presupuesto_total_año(peliculas, 2000) == 0

def test_encuentra_pelicula_mayor_recaudacion():
    peliculas = PELICULAS_CSV.copy()
    pelicula_esperada_1 = Pelicula(
        fecha_estreno=datetime.date(2019, 5, 2), 
        titulo='Avengers: Endgame', 
        director='Anthony Russo', 
        genero=['Acción', 'Aventura', 'Fantasía'], 
        duracion=181, 
        presupuesto=356, 
        recaudacion=2798, 
        reparto=['Robert Downey Jr.', 'Chris Evans', 'Mark Ruffalo']
    )
    pelicula_esperada_2 = Pelicula(
        fecha_estreno=datetime.date(2014, 11, 7), 
        titulo='Interstellar', 
        director='Christopher Nolan', 
        genero=['Drama', 'Aventura', 'Ciencia ficción'], 
        duracion=169, 
        presupuesto=165, 
        recaudacion=677, 
        reparto=['Matthew McConaughey', 'Anne Hathaway', 'Jessica Chastain']
    )
    assert encuentra_pelicula_mayor_recaudacion(peliculas, "Acción") == pelicula_esperada_1
    assert encuentra_pelicula_mayor_recaudacion(peliculas, "Ciencia ficción") == pelicula_esperada_2
    assert encuentra_pelicula_mayor_recaudacion(peliculas, "No existe") == None

# Descomenta las llamadas de los tests que quieras ejecutar
test_lee_peliculas()
#test_existe_pelicula()
#test_todas_peliculas_director_genero()
#test_construye_lista_titulos_actor()
#test_calcula_presupuesto_total_año()
#test_encuentra_pelicula_mayor_recaudacion()
print("Todos los tests pasaron correctamente.")