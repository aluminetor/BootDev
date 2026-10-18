# Errores y excepciones en Python
# Si has llegado hasta aquí en el curso, probablemente te hayas encontrado con algunos errores en tu código de vez en cuando.
# En Python, existen dos tipos principales de errores que se pueden distinguir:
# - Errores de sintaxis
# - Excepciones

# Errores de sintaxis
# Probablemente ya sepas qué son. Un error de sintaxis simplemente significa que el intérprete de Python te está indicando que tu código no se ajusta a la sintaxis correcta de Python.
# this is not valid code, so it will error

# Si intento ejecutar esa frase como si fuera código válido, obtendré un error de sintaxis:
# this is not valid code, so it will error
#       ^
# SyntaxError: invalid syntax

# Excepciones
# Aunque tu código tenga la sintaxis correcta, aún podría generar un error al intentar ejecutarlo.
# Los errores detectados durante la ejecución se denominan "excepciones" y tu código puede gestionarlos adecuadamente.
# Incluso puedes generar tus propias excepciones cuando ocurran problemas en tu código.
# Python utiliza un patrón try-except para el manejo de errores:
#
try:
    10 / 0
except Exception:
    print("can't divide by zero")

# La división por cero genera una excepción, por lo que el bloque except se ejecuta.
# La misma excepción puede ocurrir dentro de una función:
# def divide(a, b):
#     return a / b

# El bloque try se ejecuta hasta que se produce una excepción o finaliza.
# Si se produce una excepción, la ejecución salta al bloque except, omitiendo el código restante en try.
# Utilice 'as' para acceder a los datos de la excepción:
#
try:
    divide(10, 0)
    print("division complete")
except Exception as e:
    print(e)

print("done")
# ¿Qué imprime?
# division by zero
# done

# Un bloque try/except permite que el programa gestione las excepciones de forma adecuada sin que se bloquee.
# Colocar código dentro de un bloque try/except se suele denominar "envolver" el código en él.

# Asignación:
# Una de las llamadas get_player_record generará una excepción: player id not found
# 1. Coloca las cinco llamadas a funciones existentes en un solo bloque try.
# 2. Agregue un bloque except que imprima la excepción.

def main():
    try:
        print(get_player_record(1))
        print(get_player_record(2))
        print(get_player_record(3))
        print(get_player_record(4))
        print(get_player_record(5))
    except Exception as e:
        print(e)


# Don't edit below this line


def get_player_record(player_id):
    if player_id == 1:
        return {"name": "Slayer", "level": 128}
    if player_id == 2:
        return {"name": "Dorgoth", "level": 300}
    if player_id == 3:
        return {"name": "Saruman", "level": 4000}
    if player_id == 5:
        return {"name": "Gandalf", "level": 5000}
    raise Exception("player id not found")


main()
