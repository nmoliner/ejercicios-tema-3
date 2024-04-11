class Pokemon:
    def __init__(self, numero, nombre, tipo):
        self.numero = numero
        self.nombre = nombre
        self.tipo = tipo

# Función para ordenar los Pokémons por número usando el método de ordenamiento por conteo
def ordenar_por_numero(pokemons):
    max_numero = max(pokemon.numero for pokemon in pokemons)
    conteo = [0] * (max_numero + 1)
    for pokemon in pokemons:
        conteo[pokemon.numero] += 1
    sorted_pokemons = []
    for numero, cantidad in enumerate(conteo):
        sorted_pokemons.extend([pokemon for pokemon in pokemons if pokemon.numero == numero] * cantidad)
    return sorted_pokemons

# Función para ordenar los Pokémons por nombre usando el método de ordenamiento rápido (quicksort)
def ordenar_por_nombre(pokemons):
    if len(pokemons) <= 1:
        return pokemons
    pivote = pokemons[len(pokemons) // 2].nombre
    menores = [pokemon for pokemon in pokemons if pokemon.nombre < pivote]
    iguales = [pokemon for pokemon in pokemons if pokemon.nombre == pivote]
    mayores = [pokemon for pokemon in pokemons if pokemon.nombre > pivote]
    return ordenar_por_nombre(menores) + iguales + ordenar_por_nombre(mayores)

# Función para mostrar toda la información de un Pokémon dado su número
def mostrar_info_pokemon_numero(pokemons, numero):
    for pokemon in pokemons:
        if pokemon.numero == numero:
            print("Información del Pokémon número", numero)
            print("Nombre:", pokemon.nombre)
            print("Tipo:", pokemon.tipo)
            return
    print("No se encontró ningún Pokémon con el número", numero)

# Función para listar todos los Pokémons que comienzan con la letra T
def listar_pokemons_con_letra(pokemons, letra):
    pokemons_con_letra = [pokemon for pokemon in pokemons if pokemon.nombre.startswith(letra)]
    return pokemons_con_letra

# Función para determinar si un Pokémon existe y mostrar su información
def buscar_pokemon(pokemons, nombre_pokemon):
    for pokemon in pokemons:
        if pokemon.nombre.lower() == nombre_pokemon.lower():
            print("Se encontró el Pokémon", nombre_pokemon)
            print("Número:", pokemon.numero)
            print("Tipo:", pokemon.tipo)
            return
    print("No se encontró ningún Pokémon llamado", nombre_pokemon)

# Función para listar todos los Pokémon de tipo eléctrico y contar cuántos son
def listar_pokemons_tipo_electrico(pokemons):
    electricos = [pokemon for pokemon in pokemons if pokemon.tipo.lower() == "eléctrico"]
    cantidad_electricos = len(electricos)
    return electricos, cantidad_electricos

# Crear una lista de Pokémon
pokemons = [
    Pokemon(25, "Pikachu", "Eléctrico"),
    Pokemon(143, "Snorlax", "Normal"),
    Pokemon(385, "Jirachi", "Psíquico"),
    Pokemon(640, "Zekrom", "Eléctrico"),
    Pokemon(641, "Reshiram", "Fuego"),
    Pokemon(642, "Cobalion", "Acero"),
    Pokemon(702, "Dedenne", "Eléctrico"),
    Pokemon(736, "Grubbin", "Bicho"),
    Pokemon(789, "Cosmog", "Psíquico"),
    Pokemon(886, "Dracozolt", "Eléctrico")
]

# Tarea 1: Mostrar un listado de los Pokémons ordenados por números usando el método de ordenamiento por conteo
print("Pokémons ordenados por número:")
for pokemon in ordenar_por_numero(pokemons):
    print(pokemon.numero, pokemon.nombre)

# Tarea 2: Realizar un listado ordenado por nombre utilizando el método de ordenamiento rápido
print("\nPokémons ordenados por nombre:")
for pokemon in ordenar_por_nombre(pokemons):
    print(pokemon.nombre)

# Tarea 3: Mostrar toda la información del Pokémon número 640
print("\nInformación del Pokémon número 640:")
mostrar_info_pokemon_numero(pokemons, 640)

# Tarea 4: Listar todos los Pokémons que comienzan con la letra T
print("\nPokémons que comienzan con la letra T:")
for pokemon in listar_pokemons_con_letra(pokemons, "T"):
    print(pokemon.nombre)

# Tarea 5: Determinar si existe el Pokémon Cobalion y mostrar toda su información
print("\nInformación del Pokémon Cobalion:")
buscar_pokemon(pokemons, "Cobalion")

# Tarea 6: Realizar un listado de todos los Pokémon de tipo eléctrico y calcular cuántos son
electricos, cantidad_electricos = listar_pokemons_tipo_electrico(pokemons)
print("\nPokémons de tipo eléctrico:")
for pokemon in electricos:
    print(pokemon.nombre)
print("Cantidad total de Pokémons de tipo eléctrico:", cantidad_electricos)
