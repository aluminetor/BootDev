# ==============================================================================
# MÓDULO 7: ALCANCE DE LAS VARIABLES (SCOPE)
# ==============================================================================
# El alcance (scope) define en qué partes del código existe y es accesible
# una variable o función.

# ------------------------------------------------------------------------------
# 7.1 Ámbito Local (Local Scope)
# ------------------------------------------------------------------------------
# Las variables y parámetros creados DENTRO de una función solo existen dentro
# de ella. Intentar acceder a ellos desde fuera provoca un NameError.

def subtract(x, y):
    # `x` y `y` nacen aquí y mueren cuando la función termina
    return x - y

result = subtract(5, 3)
print("Resultado de subtract:", result)
# print(x)  # <-- Descomentar esto lanza: NameError: name 'x' is not defined


# Ejercicio: Cálculo de salud máxima (pasando variables globales como argumentos)
def get_max_health(modifier, level):
    return modifier * level

my_modifier = 5
my_level = 10

max_health = get_max_health(my_modifier, my_level)
print(f"max_health is: {max_health}")
print("-------------------------------------")


# ------------------------------------------------------------------------------
# 7.2 Ámbito Global (Global Scope)
# ------------------------------------------------------------------------------
# Las variables definidas fuera de cualquier función (al nivel principal del
# archivo) son globales: cualquier función puede leerlas directamente.

player_level = 4  # Variable global

def calculate_health(modifier):
    # Lee `player_level` directamente desde el ámbito global
    return player_level * modifier

def calculate_primary_stats(armor_bonus, modifier):
    return armor_bonus + modifier + player_level

print(f"Character has {calculate_health(10)} max health.")
print(f"Character has {calculate_primary_stats(3, 8)} primary stats.")
print("=====================================")
