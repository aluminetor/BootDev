# ==============================================================================
# MÓDULO 1: FUNDAMENTOS Y SINTAXIS BÁSICA
# ==============================================================================
# Las funciones permiten reutilizar código sin repetirlo.
# - `def`: palabra clave para definir la función.
# - Parámetros: variables de entrada entre paréntesis.
# - `return`: finaliza la función y devuelve un resultado.

def area_of_circle(radius):
    pi = 3.14
    area = pi * radius * radius
    return area


# Uso de la función con diferentes argumentos:
sword_length = 1.0
spear_length = 2.0

sword_area = area_of_circle(sword_length)
spear_area = area_of_circle(spear_length)

print("Sword length:", sword_length, "meters.")
print("Sword attack area:", round(sword_area, 2), "square meters")
print("Spear length:", spear_length, "meters.")
print("Spear attack area:", round(spear_area, 2), "square meters")
print("=====================================")


# ==============================================================================
# MÓDULO 2: PARÁMETROS VS. ARGUMENTOS Y MÚLTIPLES ENTRADAS
# ==============================================================================
# - Parámetros: los nombres en la definición de la función (ej. a, b).
# - Argumentos: los valores reales que pasas al llamarla (ej. 5, 3).

def subtract(a, b):
    return a - b

print("Resta:", subtract(5, 3))


def create_introduction(name, age, height):
    return f"Hello, {name}! You are {age} years old and {height} meters tall."

print(create_introduction("aluminetor", 322, 2.4))


# Ejercicio: Triple Attack
def triple_attack(damage_one, damage_two, damage_three):
    return damage_one + damage_two + damage_three

print("Triple attack 1:", triple_attack(2, 4, 3), "points of damage dealt!")
print("Triple attack 2:", triple_attack(-1, 10, 5), "points of damage dealt!")
print("=====================================")


# ==============================================================================
# MÓDULO 3: IMPRESIÓN (print) VS. DEVOLUCIÓN (return)
# ==============================================================================
# - `print()`: muestra un valor en consola, pero devuelve `None`.
# - `return`: entrega un valor al código que llamó a la función (no imprime nada).

def print_alchemy():
    print("equivalent exchange")

def return_transmutation():
    return "nothing is lost"

printed_val = print_alchemy()       # Imprime el texto y guarda None
print("Valor guardado de print_alchemy:", printed_val)

returned_val = return_transmutation() # Guarda el texto sin imprimirlo
print("Valor guardado de return_transmutation:", returned_val)
print("=====================================")


# ==============================================================================
# MÓDULO 4: FLUJO DE EJECUCIÓN Y ORDEN DE FUNCIONES
# ==============================================================================
# Una función puede llamar a otras funciones. El punto de entrada (`main()`)
# siempre se llama al final, una vez que todas las funciones ya fueron definidas.

def main_health_flow():
    health = 10
    armor = 5
    add_armor(health, armor)

def add_armor(h, a):
    new_health = h + a
    print_health(new_health)

def print_health(new_health):
    print(f"The player now has {new_health} health")

main_health_flow()
print("=====================================")


# ==============================================================================
# MÓDULO 5: PARÁMETROS PREDETERMINADOS (OPCIONALES)
# ==============================================================================
# Se asigna un valor por defecto en la firma usando `=`. Si no se envía ese
# argumento al llamar la función, tomará el valor predeterminado.

def get_greeting(email, name="there"):
    print(f"Hello {name}, welcome! You've registered your email: {email}")

get_greeting("lane@example.com", "Lane")
get_greeting("lane@example.com")


# Ejercicio: Punch & Slash con armadura opcional
def get_punched(health, armor=0):
    damage = 50 - armor
    return health - damage

def get_slashed(health, armor=0):
    damage = 100 - armor
    return health - damage

print("Health after punch (armor 5):", get_punched(400, 5))
print("Health after punch (no armor):", get_punched(400))
print("Health after slash (armor 3):", get_slashed(300, 3))
print("Health after slash (no armor):", get_slashed(300))
print("=====================================")


# ==============================================================================
# MÓDULO 6: MÚLTIPLES VALORES DE RETORNO
# ==============================================================================
# Una función puede devolver varios valores separados por comas. Al llamarla,
# se desempaquetan en el mismo orden en que fueron devueltos.

def cast_iceblast(wizard_level, start_mana):
    damage = wizard_level * 2
    new_mana = start_mana - 10
    return damage, new_mana

damage, mana = cast_iceblast(5, 100)
print(f"Damage: {damage}, Remaining Mana: {mana}")


# Ejercicio: Become Warrior
def become_warrior(full_name, power):
    title = f"{full_name} the warrior"
    new_power = power + 1
    return title, new_power

warrior_title, warrior_power = become_warrior("Frodo Baggins", 5)
print(f"{warrior_title} has a power level of: {warrior_power}")


# Ejercicio: Enchant and Attack
def enchant_and_attack(target_health, damage, weapon):
    enchanted_damage = damage + 10
    new_health = target_health - enchanted_damage
    enchanted_weapon = f"enchanted {weapon}"
    return enchanted_weapon, new_health

w_name, remaining_hp = enchant_and_attack(100, 50, "sword")
print(f"Attacked with {w_name}. Target remaining health: {remaining_hp}")
