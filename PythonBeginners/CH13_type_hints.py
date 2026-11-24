"""Capítulo 13: Sugerencias de tipo en Python

Las sugerencias de tipo documentan qué valores esperan las funciones y qué valores devuelven. También ayudan al editor a ofrecer autocompletado y a los verificadores estáticos a detectar errores antes de ejecutar el programa.

Importante: Python no valida automáticamente los tipos anotados. Por ejemplo, level: int expresa que se espera un entero, pero la anotación por sí sola no impide que alguien pase una cadena.

Organicé el capítulo de lo básico a lo avanzado, eliminé definiciones repetidas y conservé la lógica de los ejercicios.

1. Tipos básicos
Para anotar una variable, escribe nombre: tipo = valor.

Python
character_name: str = "Gandalf"
character_level: int = 80
character_health: float = 99.5
has_magic: bool = True
En asignaciones simples, el editor o el verificador de tipos suele poder inferir el tipo a partir del valor. Por ejemplo, en character_health = 99.5 puede inferir que es float.

2. Parámetros de una función
Para anotar un parámetro, escribe nombre: tipo dentro de los paréntesis.

Python
def greet_player(name: str):
    print(f"Welcome, {name}!")
Ejercicio resuelto: anotar los cuatro parámetros de get_character_status sin modificar el cuerpo.

Python
def get_character_status(
    name: str,
    level: int,
    health: float,
    has_magic: bool,
):
    status = f"{name} is level {level} with {health} HP"

    if has_magic:
        status += ", and can cast spells"
    else:
        status += ", and cannot cast spells"

    return status


print(get_character_status("Gandalf", 80, 99.5, True))
3. Tipos de retorno
La anotación de retorno va después de los parámetros y antes de los dos puntos: -> tipo.

Python
def add_gold(current_gold: int, found_gold: int) -> int:
    return current_gold + found_gold


def surface_area_of_cube(edge_length: float) -> str:
    return f"The surface area of the cube is {6 * edge_length ** 2}."

Fíjate en el segundo ejemplo: aunque la función hace un cálculo, devuelve una cadena, no un número.

Ejercicio resuelto: agregar -> str a get_item_description.

Python
def get_item_description(
    item_name: str,
    damage: int,
    is_magical: bool,
) -> str:
    description = f"{item_name} deals {damage} damage"

    if is_magical:
        description += " and glows with arcane power"
    else:
        description += " and has no magical properties"

    return description


print(get_item_description("Sword of Destiny", 15, True))
4. Corrección de anotaciones
La anotación debe coincidir con el valor que realmente devuelve la función. Como get_greeting devuelve texto, su retorno debe ser str.

Python
def get_greeting(player_name: str) -> str:
    return f"Welcome, {player_name}!"
5. Listas y conjuntos
list[str]: lista de cadenas; puede contener duplicados.
set[str]: conjunto de cadenas; elimina los duplicados y no garantiza un orden de presentación.
Ejercicio resuelto: recibir una lista de objetos y devolver un conjunto con los nombres únicos.

Python
def get_unique_items(inventory: list[str]) -> set[str]:
    unique_items = set()

    for item in inventory:
        unique_items.add(item)

    return unique_items


print(get_unique_items(["Iron Sword", "Healing Potion", "Iron Sword"]))
6. Diccionarios
La sintaxis es dict[tipo_de_clave, tipo_de_valor]. Por ejemplo, dict[str, int] relaciona nombres de objetos con cantidades enteras.

Ejercicio resuelto: devolver la cantidad de un objeto o 0 si no aparece en el inventario.

Python
def get_item_count(item_counts: dict[str, int], item_name: str) -> int:
    if item_name in item_counts:
        return item_counts[item_name]
    return 0


item_counts: dict[str, int] = {
    "Wooden Arrow": 30,
    "Small Amethyst": 2,
}

print(get_item_count(item_counts, "Wooden Arrow"))
7. Tuplas
En una anotación como tuple[str, int], cada posición tiene su propio tipo: primero una cadena, luego un entero.

Python
drop: tuple[str, int] = ("Garnet Mark", 2)
stats: tuple[int, float, int] = (100, 42.5, 75)
Ejercicio resuelto: devolver el nombre del botín y su cantidad.

Python
def get_loot_drop(enemy_level: int) -> tuple[str, int]:
    if enemy_level > 10:
        return "Emerald Brome", 1

    return "Smokestone Chip", 3


print(get_loot_drop(12))
8. Contenedores con tipos específicos
list indica que un valor es una lista, pero no describe sus elementos. list[str] también permite que el verificador infiera que items[0] es una cadena.

Ejercicio resuelto: especificar los tipos de items, item_counts y el retorno.

Python
def get_reward_summary(
    items: list[str],
    item_counts: dict[str, int],
) -> tuple[str, int]:
    total_items = 0

    for count in item_counts.values():
        total_items += count

    first_item = items[0]
    return first_item, total_items


print(
    get_reward_summary(
        ["Black Firebomb", "Titanite Chunk"],
        {"Black Firebomb": 1, "Titanite Chunk": 2},
    )
)

Nota: list[str] no garantiza que la lista tenga elementos. Esta función presupone que items no está vacía.

9. Tipos anidados
Lee las anotaciones de afuera hacia adentro. dict[str, list[str]] es un diccionario cuyas claves son cadenas y cuyos valores son listas de cadenas.

Python
character_spells: dict[str, list[str]] = {
    "Gandalf": ["Fireball", "Light"],
    "Frodo": ["Hide"],
}
10. Valores opcionales con None
El operador | indica que un valor puede pertenecer a cualquiera de los tipos anotados. Por ejemplo, int | None significa «un entero o None».

damage_bonus: int | None = None
Ejercicio resuelto: devolver el nombre de la montura si se puede invocar; de lo contrario, devolver None.

Python
def summon_mount(has_mount: bool, distance: int) -> str | None:
    if not has_mount:
        return None

    if distance > 420:
        return None

    return "Battle Horse"


print(summon_mount(True, 400))   # Battle Horse
print(summon_mount(False, 400))  # None
11. Ejercicio integrador: recompensas de misiones
La función recibe una lista de misiones completadas y un diccionario de recompensas. Devuelve list[tuple[str, int]]: una lista de pares (misión, XP). Si una misión no aparece en el diccionario, no se incluye en el resultado.

Python
def summarize_quest_rewards(
    completed_quests: list[str],
    quest_rewards: dict[str, int],
) -> list[tuple[str, int]]:
    summary: list[tuple[str, int]] = []

    for quest_name in completed_quests:
        if quest_name in quest_rewards:
            quest_xp: tuple[str, int] = (
                quest_name,
                quest_rewards[quest_name],
            )
            summary.append(quest_xp)

    return summary


print(
    summarize_quest_rewards(
        ["Dragon Slayer", "Goblin Hunt"],
        {"Dragon Slayer": 500, "Goblin Hunt": 200},
    )
)
# [('Dragon Slayer', 500), ('Goblin Hunt', 200)]
"""
