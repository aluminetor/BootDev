# Ganancias del concierto
# Calcula las ganancias de un pequeño concierto utilizando las variables proporcionadas. Mantén sus valores iniciales sin cambios.

# Crear revenue: el dinero ganado con la venta de todas las entradas.
# Crear total_cost: el costo del lugar más el costo del equipo.
# Crear profit: los ingresos restantes después de pagar el costo total.
# Utilice f-strings para imprimir estos tres valores en orden, con las etiquetas que se muestran a continuación.
# Formato de salida (reemplace cada marcador de posición con su valor calculado):

tickets_sold = 80
ticket_price = 15
venue_cost = 500
equipment_cost = 180
revenue = ticket_price * tickets_sold 
total_cost = venue_cost + equipment_cost
profit = revenue - total_cost 
print(f"Revenue: {revenue}")
print(f"Cost: {total_cost}")
print(f"Profit: {profit}")

"""
Libro de hechizos
A medida que avances en Boot.dev, es posible que desees:

Tomar apuntes
Repase los conceptos que ya ha aprendido.
Ver más ejemplos de un concepto
Vea un ejemplo de sintaxis que ya ha aprendido.
Tu libro de hechizos resuelve estos problemas .

Es una guía rápida con función de búsqueda que incluye todo lo que has aprendido en Boot.dev. A medida que completes las lecciones, desbloquearás automáticamente nuevas páginas en tu libro de hechizos, las cuales podrás consultar en cualquier momento. Así que, si sabes lo que buscas, usa tu libro de hechizos antes de hablar con Boots, ¡porque usarlo no cuesta objetos ni puntos de experiencia!
"""
#Los jugadores de Fantasy Quest, conocidos como Ballan's Ballers, han ganado todas sus partidas en la ronda eliminatoria del torneo. ¡Ahora están en la final! Calcula la puntuación media de sus 4 partidas y guárdala en la average_scorevariable.

game_one_score = 97
game_two_score = 92
game_three_score = 106
game_four_score = 105

# Don't touch above this line

average_score = (game_one_score + game_two_score + game_three_score + game_four_score) / 4

# Don't touch below this line

print(round(average_score))


# Informe de personajes
# Uno de nuestros becarios creó un programa que imprime información sobre los personajes de Fantasy Quest. Está casi terminado, pero aún tiene algunos fallos.

# Asignación
# ¡Corrige los errores para que funcione el informe de personajes!

# Ejecuta el código para ver si falla.
# Corrige la sintaxis para que cada variable sea del tipo de dato que esperas:
# name:String
# level:Integer
# character_class:String
# magic_resistance( FloatCambia la asignación de variables, no la instrucción de impresión)
# account_active:Boolean
# No cambie el significado de los valores, solo la sintaxis que 

name = "Lopen"
level = 25
character_class = "Windrunner"
magic_resistance = 10.5
account_active = True

# Don't edit below this line

print("Character Report")
print(f"{name} is a level {level} {character_class}.")
print(f"They have {magic_resistance} magic resistance.")
print(f"Their account is currently active: {account_active}")

print("=========================")
print("Character Report Complete")
print("Data types:")
print(f"name: {type(name).__name__}, level: {type(level).__name__}, character_class: {type(character_class).__name__}")
print(f"magic_resistance: {type(magic_resistance).__name__}")
print(f"account_active: {type(account_active).__name__}")
"""
Búsqueda en la lista de sitios seguros
Completa la safe_getfunción .

Debe aceptar una lista y un índice. Devuelve el elemento en ese índice solo cuando el índice esté entre 0y la última posición válida en la lista.

Regresar Nonecuando:

El índice es negativo
El índice es igual o mayor que la longitud de la lista.
La lista está vacía
Ejemplos:

safe_get(["sword", "shield", "potion"], 1)
# "shield"

safe_get(["sword", "shield", "potion"], 5)
# None

Utilice la longitud de la lista y las comparaciones para comprobar el índice antes de indexar la lista.
"""


# def safe_get(items, index):
#     if index < 0 or index >= len(items):
#         return None
#     return items[index]

"""
Valores del diccionario
Un diccionario de Python almacena valores bajo claves.
"""
pet = {"name": "Milo", "age": 2}

pet["age"] = 3
"""
Piensa en cómo se utiliza la misma clave para leer y cambiar su valor.
"""
pet = {"name": "Milo", "age": 2}

pet["age"] = 3
print(pet["age"])

# Corregir reservas de asientos
# La reserve_seatsfunción debe convertir requesteduna cadena de texto a un número entero y devolver el número de asientos restantes.

# El sistema actual de gestión de excepciones devuelve resultados incorrectos en lugar de generar errores útiles.

# Comportamiento esperado
# Si requestedno es un número entero, genere una excepción ValueErrorcon el mensaje seat count must be a whole number.
# Si el número convertido es cero o negativo, genere una excepción ValueErrorcon el mensaje seat count must be positive.
# Si no hay suficientes asientos, levante un ValueErrorcon el mensaje not enough seats.
# De lo contrario, devuelva el número de asientos restantes.
# Por ejemplo:
def reserve_seats(requested, available):
    try:
        seat_count = int(requested)
    except ValueError:
        return "seat count must be a whole number"

    if seat_count <= 0:
        return "seat count must be positive"

    if seat_count > available:
        return "not enough seats"

    return available - seat_count


print("=========================")
print(reserve_seats("3", 10))  # 7
print(reserve_seats("three", 10))  # raises ValueError: seat count must be a whole number
print(reserve_seats("12", 10))  # raises ValueError: not enough
print(reserve_seats("0", 10))  # raises ValueError: seat count must be positive
print(reserve_seats("-5", 10))  # raises ValueError: seat count must be positive
print(reserve_seats("8", 8))  # 0
print(reserve_seats("15", 40))  # 25