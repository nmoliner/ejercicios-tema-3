# Lista de dioses griegos
dioses_griegos = ["Zeus", "Hera", "Poseidón", "Deméter", "Atenea", "Apolo", "Artemisa", "Ares", "Afrodita", "Hermes", "Hefesto", "Hestia", "Hades", "Dionisio"]

# Función para emitir un listado de todos los dioses ordenados
def listar_dioses_ordenados(dioses):
    return sorted(dioses)

# Función para determinar si Atenea está en la lista de dioses
def buscar_atenea(dioses):
    return "Atenea" in dioses

# Función para indicar en qué posición se encuentra Deméter
def posicion_demeter(dioses):
    return dioses.index("Deméter") + 1

# Función para listar todos los dioses que comienzan con la letra H y determinar cuántos son
def listar_dioses_con_letra(dioses, letra):
    dioses_con_letra = [dios for dios in dioses if dios.startswith(letra)]
    return dioses_con_letra, len(dioses_con_letra)

# Función para agregar al dios Helios y volver a listar los dioses ordenados alfabéticamente
def agregar_helios(dioses):
    dioses.append("Helios")
    return sorted(dioses)

# Tarea 1: Listar todos los dioses ordenados
print("Dioses griegos ordenados:")
print(listar_dioses_ordenados(dioses_griegos))

# Tarea 2: Determinar si Atenea está en la lista de dioses
print("\n¿Atenea está en la lista de dioses?")
print("Sí" if buscar_atenea(dioses_griegos) else "No")

# Tarea 3: Indicar en qué posición se encuentra Deméter
print("\nPosición de Deméter:", posicion_demeter(dioses_griegos))

# Tarea 4: Listar todos los dioses que comienzan con la letra H y determinar cuántos son
dioses_con_h, cantidad_h = listar_dioses_con_letra(dioses_griegos, "H")
print("\nDioses que comienzan con la letra H:")
print(dioses_con_h)
print("Cantidad:", cantidad_h)

# Tarea 5: Agregar al dios Helios y volver a listar los dioses ordenados alfabéticamente
print("\nAgregar a Helios y volver a listar los dioses:")
dioses_griegos_con_helios = agregar_helios(dioses_griegos)
print(dioses_griegos_con_helios)
