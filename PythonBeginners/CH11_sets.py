# Conjuntos
# Los conjuntos son como las listas, pero no tienen un orden específico y garantizan la unicidad . Solo puede haber UNO de cada valor en un conjunto.
fruits = {"apple", "banana", "grape"}
print(type(fruits))  # Prints: <class 'set'>
print(fruits)  # Prints: {'banana', 'grape', 'apple'}


# Agregar valores
# Puedes .add()agregar valores a un conjunto. ¡Piensa en .add()algo similar append, pero para conjuntos!
fruits = {"apple", "banana", "grape"}
fruits.add("pear")
print(fruits)  # Prints: {'pear', 'banana', 'grape', 'apple'}

# No se producirá ningún error si añade un elemento que ya está en el conjunto, y el conjunto permanecerá sin cambios.

# Un conjunto vacío
# Debido a que la sintaxis de corchetes vacíos {}crea un diccionario vacío, para crear un conjunto vacío , debe utilizar la set()función.
fruits = set()
fruits.add("pear")
print(fruits)  # Prints: {'pear'}


# Iteración de conjuntos
fruits = {"apple", "banana", "grape"}
for fruit in fruits:
    print(fruit)
    # Prints:
    # banana
    # grape
    # apple

# Nota: Los conjuntos no están ordenados, por lo que no se garantiza el orden de iteración .

# Conversión de colecciones
# La set()función puede convertir una lista en un conjunto y list()viceversa:
fruits = ["apple", "banana", "apple"]
unique_fruits = set(fruits)
fruits = list(unique_fruits)


# Asignación
# Completa la remove_duplicatesfunción. Debe tomar una lista de hechizos que un jugador ha aprendido y devolver una nueva lista Listdonde haya como máximo una copia de cada título. Puedes lograr esto de al menos dos maneras:
# Iteración:
# 1. Crea un conjunto para rastrear los hechizos que se han visto
# 2. Crea una lista para almacenar los hechizos únicos.
# 3. Iterar sobre la lista
#   1. Si el hechizo no está en el conjunto, agréguelo al conjunto y a la lista.
# 4. Devuelve la lista
# Conversión de conjuntos:
# 1. Convierte la lista en un conjunto

# def remove_duplicates(spells):
#     seen = set()
#     deduped_spells = []
#     for spell in spells:
#         if spell not in seen:
#             seen.add(spell)
#             deduped_spells.append(spell)
#     return deduped_spells


# def alt_remove_duplicates(spells):
#     return list(set(spells))


"""
# 2. Convierte el conjunto de nuevo en una lista y devuélvela.
# ¡No tiene sentido aprender un hechizo dos veces! Una vez aprendido, se aprende para siempre.
"""

def remove_duplicates(spells):
    trans = set(spells)
    return sorted(list(trans))


print(remove_duplicates(["fireball", "eldritch blast", "fireball", "eldritch blast", "chill touch", "eldritch blast", "chill touch", "chill touch", "fireball", "fireball", "shocking grasp", "fireball", "fireball"]))
print(remove_duplicates(["fireball", "fireball", "fireball"]))
print(remove_duplicates(["fireball", "eldritch blast", "chill touch", "shocking grasp"]))
print(remove_duplicates(["chill touch", "chill touch", "chill touch"]))
print(remove_duplicates(["shocking grasp", "shocking grasp", "shocking grasp"]))
print(remove_duplicates([]))
print(remove_duplicates(["eldritch blast", "eldritch blast", "eldritch blast"]))

# Eliminación de valores

fruits = {"apple", "banana", "grape"}
fruits.remove("apple")
print(fruits)
# Prints: {'banana', 'grape'}


# vocales
# El equipo anti-spam de Fantasy Quest está realizando análisis de texto en los chats de los jugadores dentro del juego.

# Asignación
# Completa la count_vowelsfunción . Recibe una cadena de texto y devuelve:

# El número total de vocales en la cadena (cuenta todas las ocurrencias, no solo las únicas).
# Un conjunto de las vocales únicas que se encuentran en la cadena
# Solo nos interesan las 5 vocales: a, e, i, o, u, y sus versiones en mayúscula . Trata las vocales en mayúscula y minúscula como independientes. Por ejemplo, "A" y "a" no son lo mismo.

def count_vowels(text):
    vowels = {"A","a","E","e","I","i","O","o","U","u"}
    count = 0
    unique = set()
    for char in text:
        if char in vowels:
            count += 1
            unique.add(char)
    return count, unique


print(count_vowels("The quick brown fox jumps over the lazy dog."))

# Resta de conjuntos
# Puedes usar algunas de las operaciones matemáticas "normales" con conjuntos. Por ejemplo, puedes restar un conjunto de otro. Esto elimina todos los valores del segundo conjunto del primero.

set1 = {"apple", "banana", "grape"}
set2 = {"apple", "banana"}
set3 = set1 - set2

print(set3)
# Prints: {'grape'}

# Asignación
# Completa la find_missing_idsfunción . Acepta dos listas como entrada y devuelve un nuevo conjunto con todos los ID que están en la primera lista pero no en la segunda.

# Naturalmente, el resultado no debería tener identificadores duplicados.