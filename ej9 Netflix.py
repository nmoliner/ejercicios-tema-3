class Serie:
    def __init__(self, nombre, temporadas, capitulos_totales):
        self.nombre = nombre
        self.temporadas = temporadas
        self.capitulos_totales = capitulos_totales

# Lista de series de Netflix
series_netflix = [
    Serie("Stranger Things", 4, 34),
    Serie("The Crown", 5, 50),
    Serie("Narcos", 3, 30),
    Serie("Breaking Bad", 5, 62),
    Serie("Money Heist", 5, 55),
    Serie("The Witcher", 2, 16),
    Serie("The Umbrella Academy", 3, 30),
    Serie("Dark", 3, 26),
    Serie("Friends", 10, 236),
    Serie("The Office", 9, 201),
    Serie("Los 100", 7, 100),
    Serie("Star Wars: Rebels", 4, 75),
    Serie("BoJack Horseman", 6, 77),
    Serie("Brooklyn Nine-Nine", 8, 153)
]

# Función para listar las series ordenadas según diferentes criterios
def listar_series_ordenadas(series, criterio):
    if criterio == "nombre":
        return sorted(series, key=lambda x: x.nombre)
    elif criterio == "temporadas":
        return sorted(series, key=lambda x: x.temporadas)
    elif criterio == "capitulos":
        return sorted(series, key=lambda x: x.capitulos_totales)

# Función para mostrar toda la información de una serie específica
def mostrar_info_serie(series, nombre_serie):
    for serie in series:
        if serie.nombre == nombre_serie:
            return serie
    return None

# Función para determinar la serie con mayor cantidad de temporadas y mayor cantidad de capítulos
def serie_mayor_temporadas_y_capitulos(series):
    mayor_temporadas = max(series, key=lambda x: x.temporadas)
    mayor_capitulos = max(series, key=lambda x: x.capitulos_totales)
    return mayor_temporadas, mayor_capitulos

# Función para calcular la cantidad de series y el promedio de temporadas
def calcular_cantidad_y_promedio_temporadas(series):
    cantidad_series = len(series)
    promedio_temporadas = sum(serie.temporadas for serie in series) / cantidad_series
    return cantidad_series, promedio_temporadas

# Función para calcular el promedio de capítulos por temporada de una serie específica
def promedio_capitulos_por_temporada(series, nombre_serie):
    for serie in series:
        if serie.nombre == nombre_serie:
            return serie.capitulos_totales / serie.temporadas
    return None

# Función para listar el TOP 5 de series con mayor cantidad de capítulos
def top_5_capitulos(series):
    return sorted(series, key=lambda x: x.capitulos_totales, reverse=True)[:5]

# Función para listar el TOP 10 de series con mayor cantidad de temporadas
def top_10_temporadas(series):
    return sorted(series, key=lambda x: x.temporadas, reverse=True)[:10]

# Función para mostrar todas las series con tres o menos temporadas
def series_tres_o_menos_temporadas(series):
    return [serie for serie in series if serie.temporadas <= 3]

# Tarea 1: Listar las series ordenadas según diferentes criterios
print("Series ordenadas por nombre:")
for serie in listar_series_ordenadas(series_netflix, "nombre"):
    print(serie.nombre)

print("\nSeries ordenadas por cantidad de temporadas:")
for serie in listar_series_ordenadas(series_netflix, "temporadas"):
    print(f"{serie.nombre}: {serie.temporadas} temporadas")

print("\nSeries ordenadas por cantidad de capítulos:")
for serie in listar_series_ordenadas(series_netflix, "capitulos"):
    print(f"{serie.nombre}: {serie.capitulos_totales} capítulos")

# Tarea 2: Mostrar toda la información de la serie "Los 100"
print("\nInformación de la serie 'Los 100':")
info_los_100 = mostrar_info_serie(series_netflix, "Los 100")
print(f"Nombre: {info_los_100.nombre}, Temporadas: {info_los_100.temporadas}, Capítulos totales: {info_los_100.capitulos_totales}")

# Tarea 3: Determinar la serie con mayor cantidad de temporadas y mayor cantidad de capítulos
serie_mayor_temp, serie_mayor_cap = serie_mayor_temporadas_y_capitulos(series_netflix)
print(f"\nSerie con mayor cantidad de temporadas: {serie_mayor_temp.nombre} ({serie_mayor_temp.temporadas} temporadas)")
print(f"Serie con mayor cantidad de capítulos: {serie_mayor_cap.nombre} ({serie_mayor_cap.capitulos_totales} capítulos)")

# Tarea 4: Calcular la cantidad de series y el promedio de temporadas
cantidad_series, promedio_temporadas = calcular_cantidad_y_promedio_temporadas(series_netflix)
print(f"\nCantidad de series en la plataforma: {cantidad_series}")
print(f"Promedio de temporadas por serie: {promedio_temporadas:.2f}")

# Tarea 5: Calcular el promedio de capítulos por temporada de la serie "Star Wars: Rebels"
nombre_serie = "Star Wars: Rebels"
promedio_capitulos_star_wars = promedio_capitulos_por_temporada(series_netflix, nombre_serie)
print(f"\nPromedio de capítulos por temporada de la serie '{nombre_serie}': {promedio_capitulos_star_wars:.2f}")

# Tarea 6: Listar el TOP 5 de series con mayor cantidad de capítulos
print("\nTOP 5 de series con mayor cantidad de capítulos:")
for serie in top_5_capitulos(series_netflix):
    print(f"{serie.nombre}: {serie.capitulos_totales} capítulos")

# Tarea 7: Listar el TOP 10 de series con mayor cantidad de temporadas
print("\nTOP 10 de series con mayor cantidad de temporadas:")
for serie in top_10_temporadas(series_netflix):
    print(f"{serie.nombre}: {serie.temporadas} temporadas")

# Tarea 8: Mostrar todas las series con tres o menos temporadas
print("\nSeries con tres o menos temporadas:")
for serie in series_tres_o_menos_temporadas(series_netflix):
    print(f"{serie.nombre}: {serie.temporadas} temporadas")

