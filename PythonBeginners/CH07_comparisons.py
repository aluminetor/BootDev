#Operadores de comparación

#Al programar es necesario poder comparar dos valores. Boolean logices el nombre para este tipo de operaciones de comparación que siempre resultan en Trueo False.
print("horse" < "cat")

# Para comparar cada carácter, Python utiliza su valor numérico en la tabla Unicode/ASCII:

# Python toma la primera letra de cada palabra: 'h' de "horse" y 'c' de "cat".
# Compara sus códigos numéricos (puedes ver el código de cualquier carácter usando la función ord()):
ord('h') # es 104
ord('c') # es 99
# Evalúa la condición:
# ¿Es 104 menor que 99 (104 < 99)? No.
# Por lo tanto, "horse" < "cat" se evalúa como False.

# En términos de orden de diccionario, "cat" va antes que "horse", por lo que "cat" se considera "menor" que "horse".

print("horse" < "cat")  # False
print("cat" < "horse")  # True

# Un detalle importante: las letras mayúsculas tienen valores numéricos menores que las minúsculas en Unicode. Por ejemplo:

print(ord('A')) # es 65
print(ord('a')) # es 97

# Sentencias condicionales

def show_status(boss_health):
    if boss_health > 0:
        print("Ganondorf is alive!")
        return
    print("Ganondorf is unalive!")

show_status(15)

# Sin un returnen el ifbloque, Ganondorf is unalivesiempre se imprimiría:

def show_status(boss_health):
    if boss_health > 0:
        print("Ganondorf is alive!")
    print("Ganondorf is unalive!")

show_status(15)

# Este código podría imprimir ambos mensajes:

# Ganondorf is alive!
# Ganondorf is unalive!

"""
Cuando solo quieras ifque se ejecute el código dentro de un bloque, usa returnpara salir de la función anticipadamente.
"""

def print_status(player_health):
    if player_health <= 0:
        print("dead")
        
    print("status check complete")


# Don't edit below this line


def test(health):
    print(f"Player Health: {health}")
    print("Checking status...")
    print_status(health)
    print("=====================================")


def main():
    test(0)
    test(5)
    test(-1)
    test(3)


main()

# Asignación
# Completa la check_swords_for_armyfunción. Si el número de espadas y el número de soldados coinciden, devuelve la cadena:

# correct amount

# De lo contrario, devuelve la cadena:

# incorrect amount

# ¡La puntuación importa! Asegúrate de devolver las cadenas exactamente como aparecen arriba.

def check_swords_for_army(number_of_swords, number_of_soldiers):
    if number_of_soldiers == number_of_swords:
        return "correct amount"
    return "incorrect amount"

# Si-Si no
# Una ifinstrucción puede ir seguida de cero o más elifinstrucciones (que significan "else if"), que a su vez pueden ir seguidas de cero o una elseinstrucción.

# Por ejemplo:
score=2
high_score= 3
second_highest_score=5
third_highest_score=6
if score > high_score:
    print("High score beat!")
elif score > second_highest_score:
    print("You got second place!")
elif score > third_highest_score:
    print("You got third place!")
else:
    print("Better luck next time")

# Primero se evalúa la ifinstrucción. Si es Trueasí, se ejecuta el cuerpo de la instrucción if y se ignoran todas las demás elifinstrucciones .else

# Si la primera ifes falsa, se evalúa la siguiente elif. Del mismo modo, si es Truefalsa, se ejecuta su cuerpo y se ignoran las demás.

# Si ninguna de las sentencias " ifo" se evalúa como verdadera, entonces solo se ejecutará el cuerpo de la sentencia final .elifTrueelse