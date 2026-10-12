### Scope

# Alcance
# El ámbito se refiere a dónde está disponible el nombre de una variable o función. Por ejemplo, cuando creamos variables dentro de una función (como al asignar nombres a nuestros parámetros), esos datos no están disponibles fuera de esa función.

# Ejemplo
def subtract(x, y):
    return x - y


result = subtract(5, 3)
# print(x)
print(result)
# ERROR! "name 'x' is not defined"

# Cuando subtractse llama a la función, asignamos el valor 5 a la variable x, pero xesta solo existe dentro del código de la subtractfunción. Si intentamos imprimir xfuera de ella, no obtendremos ningún resultado. De hecho, se producirá un error grave.

def get_max_health(modifier, level):
    return modifier * level


my_modifier = 5
my_level = 10

# don't touch above this line

max_health = get_max_health(my_modifier, my_level)

# don't touch below this line

print(f"max_health is: {max_health}")

### Alcance global

##variable definidad de forma global
player_level = 4

def calculate_health(modifier):
    return player_level * modifier


def calculate_primary_stats(armor_bonus, modifier):
    return armor_bonus + modifier + player_level


print(f"Character has {calculate_health(10)} max health.")

print(f"Character has {calculate_primary_stats(3, 8)} primary stats.")
