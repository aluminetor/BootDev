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
"""
Assignment
We need a way for our game to track whether a character's attack hits or misses.

Complete the does_attack_hit function. The function should return True if either of the following conditions is met:

The attack_roll is not a 1 and the attack_roll is greater than or equal to the armor_class, or
The attack_roll is a 20
Otherwise, it should return False.

Tip
"""
# def does_attack_hit(attack_roll, armor_class):
#     return attack_roll != 1 and attack_roll >= armor_class or attack_roll == 20
    
"""
Deberían servir bebidas
¿Crees que entiendes las condicionales? ¡Prepárate para invertir tu lógica!

Asignación
En Fantasy Quest, los jugadores pueden ir al pub local de un pueblo. ¡Beber cerveza virtual les repone la energía!

Completa la función que determina si un camarero debe servir bebidas a un cliente. Devuelve solo Truesi se cumplen todas estas condiciones. Si alguna de estas condiciones no se cumple False, devuelve False:

La edad del cliente es de 21 años o más.
El camarero está trabajando
La hora es entre las 5 y las 10 (ambas inclusive).
"""
def should_serve_customer(customer_age, on_break, time):
    if customer_age >= 21:
        if on_break == False:
            if time in range(5,11):
                return True

    return False

"""
Alquiler de la montaña
Los jugadores pueden alquilar las monturas voladoras de otros jugadores a través del gremio de viajes compartidos "Uper", pero deben devolver la montura antes de que se les acabe el tiempo, o se les cobrará una tarifa.

Asignación
Completa la check_mount_rentalfunción . Requiere dos entradas:

time_used– el tiempo que se ha utilizado el soporte en minutos
time_purchased– la cantidad de tiempo que el personaje alquiló la montura
Si time_used cumple o supera time_purchased , entonces el alquiler ha expirado y el codicioso Uper cobrará una tarifa, por lo que la función debe devolver la cadena"overtime charged"
De lo contrario, devuelve la cadena."no charges yet"
Extra: Intenta lograr esto sin una instrucción "else".
"""
def check_mount_rental(time_used, time_purchased):
    if time_used >= time_purchased:
        return "overtime charged"
    return "no charges yet"

"""
Ventaja en combate
Fantasy Quest no ofrece a los jugadores ninguna forma de saber si son lo suficientemente fuertes como para defenderse de ciertos enemigos.

Si el nivel de poder de un jugador es mayor que la defensa del enemigo, ese jugador tiene una "ventaja".
Si el poder del jugador y la defensa del enemigo son iguales, están "igualados".
De lo contrario, ese jugador tiene una "desventaja" .
Asignación
Completa combat_evaluationcon un if/elif/elsebloque que compara player_powery enemy_defenseutiliza las reglas anteriores. Las tres variables de resultado comienzan como False.

Establezca la evaluación de coincidencia ( advantage, disadvantage, o evenly_matched) en True.
Deja el valor existente returnal final para devolver los tres valores. No devuelvas nada desde ramas individuales.
"""
def combat_evaluation(player_power, enemy_defense):
    advantage, disadvantage, evenly_matched = False, False, False

    if player_power > enemy_defense:
        advantage = True
    elif player_power == enemy_defense:
        evenly_matched = True
    else:
        disadvantage = True

        
    return advantage, disadvantage, evenly_matched

