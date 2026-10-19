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

# Sugerencias de tuplas
# Las listas y los conjuntos suelen contener múltiples valores del mismo tipo:

inventory: list[str] = ["Black Knight Halberd", "Skull Lantern", "Notched Whip"]

# Pero las tuplas son un pequeño grupo fijo de valores donde cada posición tiene su propio significado. Debido a que son fijos, es bastante común que esos valores sean de diferentes tipos. Por ejemplo, un botín podría tener un nombre de objeto y una cantidad:

drop: tuple[str, int] = ("Garnet Mark", 2)

# tuple[str, int]medio:

# Hay dos valores en la tupla
# El primer valor es una cadena
# El segundo valor es un número entero.
# Una tupla puede tener cualquier número de valores, aunque 2y 3son los más comunes. Aquí hay un ejemplo que representa los HP, MP y resistencia de un personaje:

stats: tuple[int, float, int] = (100, 42.5, 75)

# La sugerencia de tipo tuple[int, float, int]nos indica que se trata de una tupla de tres valores: un entero, un número decimal y otro entero.

# Asignación
# Fantasy Quest utiliza el botín obtenido para determinar qué objetos recibe el jugador tras derrotar a un enemigo en combate. Añade sugerencias de tipo a la get_loot_dropfunción.

# Agregue una intsugerencia de tipo al enemy_levelparámetro.
# Agregue una tuple[str, int]sugerencia sobre el tipo de retorno.
# No modifique el cuerpo de la función.

def get_loot_drop(enemy_level: int)-> tuple[str, int]:
    if enemy_level > 10:
        return "Emerald Brome", 1

    return "Smokestone Chip", 3
print(get_loot_drop(12))


# Tipos de contenedores específicos
# Es posible indicar el tipo de un contenedor simplemente especificando su tipo:

items: list = ["Black Firebomb", "Titanite Chunk"]

# Esto dice itemsque es una lista, ¡pero no nos dice qué tipo de valores contiene! Suponiendo que sabes lo que hay dentro, lo mejor es ser específico:

items: list[str] = ["Black Firebomb", "Titanite Chunk"]

# Dicho esto, las sugerencias de tipo de contenedor sin especificar el tipo no son incorrectas . A veces, realmente no se sabe qué tipos de valores contendrá un contenedor, o la sugerencia de tipo específica sería demasiado compleja para ser útil. Esto se observa ocasionalmente con dictlos contenedores. ¡Simplemente proporcione sugerencias de tipo claras siempre que sea posible!

# Asignación
# La función de resumen de recompensas de Fantasy Quest ya incluye sugerencias de tipo, pero algunos tipos de contenedores son demasiado vagos. Haga que las sugerencias de tipo de contenedor sean más específicas.

# Actualización itemsde lista list[str].
# Observa que antes de agregar la sugerencia, el first_itemtipo de información sobre herramientas de la variable es "Desconocido". Después de agregar la sugerencia, Python puede inferir que first_itemes un tipo strporque está en la itemslista.

# Actualización item_countsde dicta dict[str, int].
# Actualiza el tipo de retorno de la función de tuplea tuple[str, int].
# No modifique el cuerpo de la función.

def get_reward_summary(items: list[str], item_counts: dict[str,int]) -> tuple[str,int]:
    total_items = 0

    for count in item_counts.values():
        total_items += count

    first_item = items[0]
    return first_item, total_items
print(get_reward_summary(["Black Firebomb", "Titanite Chunk"], {"Black Firebomb": 1, "Titanite Chunk": 2}))


# Tipos anidados
# Hemos visto tipos de contenedores relativamente simples como list[str], pero pueden volverse más complejos cuando un contenedor contiene otro contenedor . Es decir, es posible tener tipos de contenedores anidados .

# Un diccionario, por ejemplo, podría relacionar el nombre de cada personaje con su lista de hechizos :

character_spells: dict[str, list[str]] = {
    "Gandalf": ["Fireball", "Light"],
    "Frodo": ["Hide"],
}
# Leemos dict[str, list[str]]desde afuera hacia adentro:

# Es un diccionario ( dict)
# Cada clave es una cadena ( str)
# Cada valor es una lista de cadenas ( list[str])


# Valores opcionales
# A veces trabajamos con variables que pueden o no tener un "valor real". Por ejemplo, un personaje puede tener una bonificación de daño, o puede que no. Si no la tiene , podemos representar esa falta de valor con None.

# El |operador indica que un valor puede ser de varios tipos:

damage_bonus: int | None

# Eso significa damage_bonusque puede ser un número entero (la cantidad de bonificación) o None . Por otro ejemplo, una función podría devolver un hechizo preparado si hay uno listo, o Nonesi no hay ningún hechizo preparado:

def get_prepared_spell(has_spell: bool) -> str | None:
    if has_spell:
        return "Fireball"

    return None

# Asignación
# Los personajes de Fantasy Quest que tienen monturas propias pueden invocarlas desde una distancia limitada. Si el personaje no tiene montura, o si la montura está demasiado lejos para ser invocada, la función devuelve un valor nulo None. Añade sugerencias de tipo a la summon_mountfunción.

# Agregue una boolsugerencia de tipo al has_mountparámetro.
# Agregue una intsugerencia de tipo al distanceparámetro.
# Agregue una str | Nonesugerencia sobre el tipo de retorno.
# No modifique el cuerpo de la función.

def summon_mount(has_mount: bool, distance: int)-> str | None:
    if not has_mount:
        return None

    if distance > 420:
        return None

    return "Battle Horse"

print(summon_mount(True, 400))
print(summon_mount(False, 400))

def summarize_quest_rewards(
    completed_quests: list[str], quest_rewards: dict[str, int]
) -> list[tuple[str, int]]:
    summary: list[tuple[str, int]] = []
    for quest_name in completed_quests:
        if quest_name in quest_rewards:
            quest_xp: tuple[str, int] =(quest_name,quest_rewards[quest_name])
            summary.append(quest_xp)

    return summary
print(summarize_quest_rewards(["Dragon Slayer", "Goblin Hunt"], {"Dragon Slayer": 500, "Goblin Hunt": 200}))