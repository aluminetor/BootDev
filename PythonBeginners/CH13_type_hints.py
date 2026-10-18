"""
Capítulo 13: sugerencias de tipo.

Las sugerencias de tipo documentan los valores que reciben y devuelven las
funciones. Ayudan a leer el código, mejorar el autocompletado y detectar
errores antes de ejecutar el programa.
"""

# Algunas funciones aceptan números; otras aceptan cadenas. Algunas devuelven
# listas, diccionarios, booleanos o None.
#
# Cuando un programa crece, es fácil olvidar el tipo de una variable:
# - ¿level es un str?
# - ¿get_item() siempre devuelve un nombre o a veces devuelve None?
# - ¿inventory es una lista de cadenas o un diccionario con cantidades?
#
# Las sugerencias de tipo permiten escribir esas expectativas en el código.


def get_damage(weapon: dict, level: int) -> int:
    return weapon["damage"] + (level * 2)


print(get_damage({"name": "sword", "damage": 10}, 5))

# weapon: dict, level: int y -> int son sugerencias de tipo. Indican qué
# valores espera y devuelve la función, pero no cambian el tipado dinámico de
# Python ni rechazan automáticamente valores incorrectos.
#
# Las sugerencias de tipo sirven para:
# - Hacer que el código sea más fácil de leer.
# - Ayudar al editor a autocompletar y avisar de errores.
# - Facilitar la detección de errores antes de ejecutar el código.


def surface_area_of_cube(edge_length: float) -> str:
    return f"The surface area of the cube is {6 * edge_length ** 2}."


print(surface_area_of_cube(3.5))


"""
Tipos básicos

Para agregar una sugerencia de tipo a una variable, se colocan dos puntos
después del nombre y el tipo antes del signo igual y del valor.
"""

character_name: str = "Sir Galahad"
character_level: int = 7
character_health: float = 72.5
has_magic: bool = True

# En declaraciones simples, la sugerencia puede ser redundante porque las
# herramientas infieren el tipo a partir del valor:
character_health = 72.5

# Asignación:
# El código de configuración de personajes de Fantasy Quest funciona, pero los
# tipos de variables deben coincidir con sus valores. No cambies los valores.

character_name: str = "Gandalf"
character_level: int = 80
character_health: float = 99.5
has_magic: bool = True


"""
Parámetros de la función

Los parámetros también pueden tener sugerencias de tipo. La sintaxis consiste
en colocar dos puntos después del nombre del parámetro y escribir el tipo.
"""


def greet_player(name: str):
    print(f"Welcome, {name}!")


def add_gold(current_gold: int, found_gold: int):
    return current_gold + found_gold


# Agregar sugerencias a variables puede ser redundante debido a la inferencia
# de tipos, pero agregarlas a los parámetros ayuda al autocompletado y a la
# comprobación de errores.
#
# Asignación:
# Agrega sugerencias de tipo a los parámetros de get_character_status:
# - name debe ser str.
# - level debe ser int.
# - health debe ser float.
# - has_magic debe ser bool.
# No modifiques el cuerpo de la función.


def get_character_status(
    name: str, level: int, health: float, has_magic: bool
):
    status = f"{name} is level {level} with {health} HP"

    if has_magic:
        status += ", and can cast spells"
    else:
        status += ", and cannot cast spells"

    return status


print(get_character_status("Gandalf", 80, 99.5, True))


"""
Tipos de retorno

También se puede anotar el tipo que se espera que devuelva una función. El
tipo de retorno va después de la lista de parámetros y antes de los dos puntos.
Se usa -> en lugar de : porque no depende del nombre de una variable interna.
"""


def add_gold(current_gold: int, found_gold: int) -> int:
    return current_gold + found_gold


def get_greeting(player_name: str) -> str:
    return f"Welcome, {player_name}!"


# Asignación:
# Fantasy Quest utiliza descripciones de artículos en los menús de las tiendas.
# Agrega una sugerencia str de retorno a get_item_description.
# No cambies el cuerpo de la función.


def get_item_description(
    item_name: str, damage: int, is_magical: bool
) -> str:
    description = f"{item_name} deals {damage} damage"

    if is_magical:
        description += " and glows with arcane power"
    else:
        description += " and has no magical properties"

    return description


print(get_item_description("Sword of Destiny", 15, True))


"""
Corrección de sugerencias de tipo

El tipo anotado debe coincidir con lo que realmente hace el código. Una
función que devuelve una cadena debe tener str como tipo de retorno.
"""


def get_quest_reward(quest_name: str, quest_xp: int) -> str:
    return f"You've earned {quest_xp} XP for completing the {quest_name} quest!"


print(get_quest_reward("Dragon Slayer", 500))

# Una sugerencia incorrecta puede ser confusa y el editor puede advertirlo.
#
# Asignación:
# La función de saludo de Fantasy Quest funciona, pero su sugerencia de retorno
# es incorrecta. Cámbiala a str sin modificar el cuerpo de la función.


def get_greeting(player_name: str) -> str:
    return f"Welcome, {player_name}!"


"""
Listas y conjuntos

Además de str, int, float y bool, se pueden anotar tipos de contenedores:
list es una secuencia mutable, set una colección de valores únicos, dict una
colección de pares clave-valor y tuple una secuencia inmutable.

Al indicar un contenedor, se especifica también el tipo de valores que contiene.
"""


inventory: list[str] = ["Iron Sword", "Healing Potion"]
unique_items: set[str] = {"Iron Sword", "Healing Potion"}

# Asignación:
# Fantasy Quest tiene una función que elimina nombres de objetos duplicados.
# Agrega list[str] al parámetro inventory y set[str] al tipo de retorno.
# No modifiques el cuerpo de la función.


def get_unique_items(inventory: list[str]) -> set[str]:
    unique_items = set()

    for item in inventory:
        unique_items.add(item)

    return unique_items


print(
    get_unique_items(
        ["Iron Sword", "Healing Potion", "Iron Sword", "Healing Potion", "Iron Sword"]
    )
)


"""
Sugerencias para diccionarios

Los diccionarios asignan claves a valores, por lo que sus sugerencias incluyen
ambos tipos: dict[key_type, value_type].

En dict[str, int], las claves son cadenas y los valores son números enteros.
Los tipos de clave más comunes son str e int; los valores pueden ser de
cualquier tipo.
"""


item_counts: dict[str, int] = {
    "Wooden Arrow": 30,
    "Small Amethyst": 2,
}

# Asignación:
# Fantasy Quest registra la cantidad de cada objeto del inventario.
# Agrega estas sugerencias de tipo a get_item_count:
# - item_counts debe ser dict[str, int].
# - item_name debe ser str.
# - El retorno debe ser int.
# No modifiques el cuerpo de la función.

def get_item_count(item_counts: dict[str, int], item_name: str) -> int:
    if item_name in item_counts:
        return item_counts[item_name]
    return 0
print(get_item_count({"Wooden Arrow": 30, "Small Amethyst": 2}, "Wooden Arrow"))
