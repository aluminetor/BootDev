# Bucles
# Los bucles son el mejor amigo del programador. Nos permiten realizar la misma operación varias veces sin tener que escribirla explícitamente cada vez.
# Un bucle "for" en Python se escribe de la siguiente manera:

for i in range(0, 10):
    print(i)

# i es una variable que toma cada valor de 0 a 9, uno a la vez. En inglés, el código dice:

# Comienza con i el signo igual 0. ( i in range(0))
# Si i es mayor o igual que 10 ( range(0, 10)), salga del bucle. De lo contrario:
# Imprimir ien la consola. ( print(i))
# Agregar 1 a i. ( rangepor defecto, se incrementa de uno en uno)
# Volver al paso 2.
# El resultado es que los números 0-9 se registran en la consola en orden.



def print_numbers():
    for i in range(0,100):
        print(i)


# Don't edit below this line


def test():
    print("Printing numbers from 0 to 99:")
    print_numbers()
    print("=====================================")


def main():
    test()


main()

"""
Espacios en blanco en Python
El cuerpo de un bucle `for` debe estar indentado; de lo contrario, se producirá un error de sintaxis. Además, cada línea del bucle debe estar indentada de la misma manera: utilizamos la convención de "4 espacios". Al pulsar la <tab>tecla, se insertarán automáticamente 4 espacios.

Los espacios en blanco son importantes en Python.
"""

#Range Continued
#La range()función que hemos estado utilizando en nuestros forbucles tiene en realidad un tercer parámetro opcional: el "paso"

for i in range(0, 10, 2):
    print(i)
# prints: de dos en dos
# 0
# 2
# 4
# 6
# 8
for i in range(3, 0, -1):
    print(i)
# prints:El parámetro "step" determina cuánto se debe agregar ien cada iteración del bucle. Incluso se puede retroceder
# 3
# 2
# 1
# Asignación
# Corrige el error en la sum_of_numbersfunción. En lugar de sumar 1 en totalcada iteración del bucle, debería sumar i. Por ejemplo, en lugar de:

# 1 + 1 + 1 + 1 + 1...

# Queremos:

# 0 + 1 + 2 + 3 + 4...

# El resultado deseado es un único número una vez que el bucle haya terminado de ejecutarse.
# def sum_of_numbers(start, end):
#     total = 0
#     for i in range(start, end):
#         total += i
        
#     return total


# Assignment
# The sum_of_odd_numbers function should calculate the sum of all the odd numbers starting at 1 up to (but not including) the given end number and return the result.

# Fix the loop so that it iterates over the correct numbers.

def sum_of_odd_numbers(end):
    total = 0
    for i in range(1,end,2):
        total += i
    return total

print(sum_of_odd_numbers(6))

# Mientras
# Python tiene otro tipo de bucle, el whileloop. Es un bucle que continúa whilemientras se cumpla una condición True. La sintaxis es simple:

# while 1:
#     print("1 evaluates to True")

# prints:
# 1 evaluates to True
# 1 evaluates to True
# (...continuing)

num = 0
while num < 3:
    num += 1
    print(num)

# Declaración de continuación
# A veces, al recorrer una secuencia en bucle, puede encontrar elementos que desea omitir . Python (como muchos lenguajes de programación) proporciona una forma de hacerlo: la continueinstrucción.

# continuesignifica "pasar directamente a la siguiente iteración de este bucle". Se omite todo lo demás que debía ocurrir en la iteración actual.

# Digamos que queremos imprimir todos los números del 1 al 50, pero omitiendo cada séptimo número. Podemos usar continueesto para hacer, llevando un registro de un contador:

# # Remember, `range` is inclusive of the start, but exclusive of the end
counter = 0
for number in range(1, 51):
    counter = counter + 1

    if counter == 7:
        counter = 0  # Reset the counter
        continue  # Skip this number

    print(number)

# Por ejemplo, si estamos calculando raíces cuadradas, podríamos querer omitir los números negativos. continueEsto nos permite pasar al siguiente número sin perder tiempo:

for number in range(-5, 5):
    if number < 0:
        continue  # Skip negatives

    print(f"The square root of {number} is {number**0.5}")
    
"""
Asignación
En Fantasy Quest, otorgamos al jugador un encantamiento por cada tres misiones que registramos. Cuanto mayor sea el número total de misiones completadas, más poderoso será el encantamiento.

Corrige la award_enchantmentsfunción. Calcula la fuerza del encantamiento (5 veces el número total de misiones completadas) e imprime un mensaje para el jugador. ¡Pero debemos asegurarnos de que esto ocurra solo una vez por cada tres misiones que iteramos dentro del bucle! Solo cuenta las misiones dentro del bucle; no te preocupes si el número total de misiones es divisible por 3.

Al inicio de la función, antes del bucle, inicializa una countervariable a 0.
Dentro del forcircuito:
Añádelo 1en countercada iteración para llevar un registro de cuántas misiones hemos visto.
Si counteres menor que 3, continuepasa a la siguiente iteración.
De lo contrario, ¡debemos haber completado 3 misiones! Reiniciar counteral 0punto anterior a la obtención del encantamiento.
"""

def award_enchantments(start, end, step):
    counter = 0
    for quest_number in range(start, end, step):
        counter +=1
        if counter < 3:
            continue
        else:
            counter = 0
            enchantment_strength = quest_number * 5
            
        print(
            f"Enchantment of strength {enchantment_strength} awarded for completing {quest_number} quests!"
        )


# Don't touch below this line


def test(start, end, step):
    print(f"Testing with quests {start} through {end - 1}:")
    award_enchantments(start, end, step)
    print("========================================")


def main():
    test(1, 11, 1)
    test(20, 24, 1)
    test(10, 12, 1)
    test(11, 19, 1)


main()

# Declaración de ruptura
# Podemos usarlo continuepara pasar a la siguiente iteración en un bucle, pero ¿qué pasa si queremos salir del bucle por completo? Ahí es donde breakentra en juego la instrucción.

for n in range(42):
    print(f"{n} * {n} = {n * n}")
    if n * n > 150:
        break
"""
Experience Points
Adventurers need experience points (XP) to level up and become stronger. We want to show the total XP a player has gained given their current level.

Each character starts with 0 XP at level 1. To reach the next level, they need to accumulate additional XP equal to their current level times 5.

For example:

At level 1, XP is 0.
To reach level 2, we need 5 XP (1 * 5) added to the current XP so far (0).
At level 2, XP is 5.
To reach level 3: we need 10 XP (2 * 5) added to the current XP so far (5).
At level 3, XP is 15.
To reach level 4: we need 15 XP (3 * 5) added to the current XP so far (15).
And so on...
To summarize the calculation in a table:

Level	XP so far	XP for next level
1	0	5
2	5	10
3	15	15
4	30	20
Assignment
Complete the calculate_experience_points function.

It accepts a level (integer) and returns the total XP a player has gained so far.

"""
def calculate_experience_points(level):
    xp = 0
    for i in range(1,level):
        if i <= level:
            xp += i * 5

    return xp

