class Pelicula:
    def __init__(self, titulo, año, recaudacion, valoracion):
        self.titulo = titulo
        self.año = año
        self.recaudacion = recaudacion
        self.valoracion = valoracion

# Lista de películas
peliculas = [
    Pelicula("Avengers: Infinity War", 2018, 2048000000, 4.8),
    Pelicula("Star Wars: The Return of Jedi", 1983, 475100000, 4.5),
    Pelicula("Iron Man", 2008, 585200000, 4.7),
    Pelicula("Iron Man 2", 2010, 623900000, 4.6),
    Pelicula("The Avengers", 2012, 1519000000, 4.9),
    Pelicula("Avengers: Age of Ultron", 2015, 1405000000, 4.6),
    Pelicula("Iron Man 3", 2013, 1215000000, 4.5),
    Pelicula("Avengers: Endgame", 2019, 2798000000, 4.9),
    Pelicula("Avengers: Civil War", 2016, 1153000000, 4.7),
    Pelicula("Thor: Ragnarok", 2017, 854000000, 4.8)
]

# Función para realizar un listado ordenado por título, año de lanzamiento y por recaudación (descendente)
def listar_peliculas_ordenadas(peliculas):
    return sorted(peliculas, key=lambda x: (x.titulo, x.año, x.recaudacion), reverse=True)

# Función para mostrar toda la información de la película que más recaudó
def pelicula_mas_recaudacion(peliculas):
    mas_recaudacion = max(peliculas, key=lambda x: x.recaudacion)
    return mas_recaudacion

# Función para listar todas las películas que tengan valoración 5
def listar_peliculas_valoracion_5(peliculas):
    return [pelicula for pelicula in peliculas if pelicula.valoracion == 5]

# Función para determinar si una película está en la lista y mostrar toda su información
def buscar_pelicula(peliculas, titulo):
    for pelicula in peliculas:
        if pelicula.titulo == titulo:
            return pelicula
    return None

# Función para indicar en qué posición se encuentra una película
def posicion_pelicula(peliculas, titulo):
    for i, pelicula in enumerate(peliculas):
        if pelicula.titulo == titulo:
            return i + 1
    return None

# Función para calcular el total recaudado por las películas que en su título incluyen la palabra "Avengers"
def total_recaudado_avengers(peliculas):
    total = sum(pelicula.recaudacion for pelicula in peliculas if "Avengers" in pelicula.titulo)
    return total

# Función para mostrar todas las películas que se estrenaron en un año específico
def peliculas_por_año(peliculas, año):
    return [pelicula for pelicula in peliculas if pelicula.año == año]

# Función para listar todas las películas que comienzan con una palabra específica
def peliculas_por_palabra(peliculas, palabra):
    return [pelicula for pelicula in peliculas if pelicula.titulo.startswith(palabra)]

# Tarea 1: Listar las películas ordenadas
print("Películas ordenadas por título, año de lanzamiento y recaudación (descendente):")
for pelicula in listar_peliculas_ordenadas(peliculas):
    print(f"Título: {pelicula.titulo}, Año: {pelicula.año}, Recaudación: ${pelicula.recaudacion}")

# Tarea 2: Mostrar toda la información de la película que más recaudó
print("\nInformación de la película con mayor recaudación:")
mas_recaudacion = pelicula_mas_recaudacion(peliculas)
print(f"Título: {mas_recaudacion.titulo}, Año: {mas_recaudacion.año}, Recaudación: ${mas_recaudacion.recaudacion}")

# Tarea 3: Listar todas las películas que tengan valoración 5
print("\nPelículas con valoración 5:")
for pelicula in listar_peliculas_valoracion_5(peliculas):
    print(f"Título: {pelicula.titulo}, Valoración: {pelicula.valoracion}")

# Tarea 4: Determinar si la película "Avengers: Infinity War" está en la lista y mostrar toda su información
titulo_buscar = "Avengers: Infinity War"
print("\nInformación de la película", titulo_buscar + ":")
pelicula_avengers = buscar_pelicula(peliculas, titulo_buscar)
if pelicula_avengers:
    print(f"Título: {pelicula_avengers.titulo}, Año: {pelicula_avengers.año}, Recaudación: ${pelicula_avengers.recaudacion}, Valoración: {pelicula_avengers.valoracion}")
else:
    print("La película no está en la lista.")

# Tarea 5: Indicar en qué posición se encuentra la película "Star Wars: The Return of Jedi"
titulo_buscar = "Star Wars: The Return of Jedi"
print("\nPosición de la película", titulo_buscar + ":", posicion_pelicula(peliculas, titulo_buscar))

# Tarea 6: Calcular el total recaudado por las películas que en su título incluyen la palabra "Avengers"
print("\nTotal recaudado por las películas de Avengers:", total_recaudado_avengers(peliculas))

# Tarea 7: Mostrar todas las películas que se estrenaron en el año 2017
print("\nPelículas estrenadas en el año 2017:")
for pelicula in peliculas_por_año(peliculas, 2017):
    print(f"Título: {pelicula.titulo}, Año: {pelicula.año}, Recaudación: ${pelicula.recaudacion}, Valoración: {pelicula.valoracion}")

# Tarea 8: Listar todas las películas que comienzan con la palabra "Iron"
palabra_buscar = "Iron"
print(f"\nPelículas que comienzan con '{palabra_buscar}':")
for pelicula in peliculas_por_palabra(peliculas, palabra_buscar):
    print(f"Título: {pelicula.titulo}, Año: {pelicula.año}, Recaudación: ${pelicula.recaudacion}, Valoración: {pelicula.valoracion}")
