## FUNCTIONS ##
# Pero queremos reutilizar nuestro código! ¿Quién quiere rehacer el mismo trabajo? ¿Y si quisiéramos calcular el área de miles de círculos? Ahí es donde las funciones resultan útiles.

# En cambio, definamos una nueva función llamada area_of_circleusando la defpalabra clave:

def area_of_circle(r):
    pi = 3.14
    result = pi * r * r
    return result


radius = 5
area = area_of_circle(radius)
print(area)

area = area_of_circle(6)
print(round(area,2))
# Toma una entrada (también conocida como "parámetro" o "argumento") llamadar
# Después de la :, las líneas con sangría forman el cuerpo de la función, es decir, el código que se ejecuta cada vez que usamos (también conocido como "llamamos") la función.
# Produce returnun único valor. En este caso, el valor almacenado en la resultvariable

# 5 entra como entradar
# El cuerpo de la función se ejecuta, almacenando 78.5en la resultvariable dentro del cuerpo de la función.
# La función devuelve la resultvariable, lo que significa que la area_of_circle(5)expresión se evalúa como78.5
# 78.5se almacena en la areavariable y luego se imprime

def area_of_circle(radius):
    pi = 3.14
    area = pi * radius * radius
    return area


sword_length = 1.0
spear_length = 2.0

# don't touch above this line

sword_area = area_of_circle(sword_length)
spear_area = area_of_circle(spear_length)

# don't touch below this line

print("Sword length:", sword_length, "meters.")
print("Sword attack area:", sword_area, "square meters")

print("Spear length:", spear_length, "meters.")
print("Spear attack area:", spear_area, "square meters")


"""
Aquí tienes una explicación cronológica de lo que sucede cuando se ejecuta el código anterior:

def area_of_circle(r):

La area_of_circlefunción está definida para su uso posterior, pero no se llama. Acepta una única entrada, con un nombre arbitrario r. El cuerpo de la función ( pi = 3.14... etc.) se ignora por ahora.

radius = 5

radiusSe crea una nueva variable llamada y se le asigna el valor 5.

area_of_circle(radius)

La area_of_circlefunción se llama con radius(en este caso 5) como entrada. Finalmente, volvemos a la definición de la función.

def area_of_circle(r):

Ahora comenzaremos a ejecutar el cuerpo de la función, y restá configurado en 5.

pi = 3.14

piSe crea una nueva variable llamada con un valor de 3.14.

result = pi * r * r

Se evalúa una operación matemática simple ( 3.14 * 5 * 5) y se almacena en la resultvariable.

return result

La variable de resultado es devuelta por la función como salida.

area = area_of_circle(radius)

El valor devuelto se almacena en una nueva variable llamada area(en este caso 78.5).

print(area)

El valor arease imprime en la consola.
"""

# Multiple Parameters
# Functions can have multiple parameters ("parameter" being a fancy word for "input"). For example, this subtract function accepts 2 parameters: a and b.

def subtract(a, b):
    result = a - b
    return result

a, b = 5, 3

resta = subtract(a,b)

print(resta)

def create_introduction(name, age, height):
    intro = f"Hello, {name}! You are {age} years old and {height} meters tall."
    return intro


#it can be called like this:
msg = create_introduction("aluminetor", 322, 2.4)

print(msg)
#-----------------------Complete the triple_attack function by returning the sum of its parameters, damage_one, damage_two, and damage_three. Remember to indent the code inside the function body.-----------------------------#

def triple_attack(damage_one, damage_two, damage_three):
    triple = damage_one + damage_two + damage_three
    return triple


# Don't touch below this line

# This is the first triple attack
attack_one = 2
attack_two = 4
attack_three = 3
first_triple_attack_damage = triple_attack(attack_one, attack_two, attack_three)

print("Getting damage for", attack_one, attack_two, "and", attack_three, "...")
print(first_triple_attack_damage, "points of damage dealt!")
print("=====================================")

# This is the second triple attack
attack_four = -1
attack_five = 10
attack_six = 5
second_triple_attack_damage = triple_attack(attack_four, attack_five, attack_six)

print("Getting damage for", attack_four, attack_five, "and", attack_six, "...")
print(second_triple_attack_damage, "points of damage dealt!")
print("=====================================")



### Impresión vs. Devolución
"""
Algunos desarrolladores novatos se quedan atascados en la diferencia entre print()y return.

Puede resultar particularmente confuso cuando el conjunto de pruebas que proporcionamos simplemente imprime la salida de sus funciones en la consola. Hace parecer que y print()son returnintercambiables, ¡pero no lo son !

print()es una función que:
Imprime un valor en la consola.
No devuelve un valor .
"""
def print_alchemy():
    print("equivalent exchange")


printed_alchemy = print_alchemy()
# equivalent exchange

print(printed_alchemy)
# None

"""
return es una palabra clave que:
Finaliza la ejecución de la función actual.
Proporciona un valor (o valores) a quien llama a la función.
No imprime nada en la consola (a menos que el valor de retorno se print()edite posteriormente).

"""
def return_transmutation():
    return "nothing is lost"


returned_transmutation = return_transmutation()

print(returned_transmutation)
# nothing is lost

### Imprimir para depurar su código
#Imprimir valores y ejecutar el código es una excelente manera de depurarlo. Puedes ver qué valores se almacenan en las distintas variables, encontrar errores y corregirlos. ¡Añade instrucciones de impresión y ejecuta el código a medida que avanzas! Es un hábito muy útil para asegurarte de que cada línea que escribes hace lo que esperas.



def get_title(first_name, last_name, job):
    title = first_name + " " + last_name + " the " + job
    return title


# Don't touch below this line


def test(first_name, last_name, job):
    title = get_title(first_name, last_name, job)
    print("First name:", first_name)
    print("Last name:", last_name)
    print("Job:", job)
    print("Title:", title)
    print("=====================================")


test("Frodo", "Baggins", "warrior")
test("Bilbo", "Baggins", "thief")
test("Gandalf", "The Grey", "wizard")
test("Aragorn", "Son of Arathorn", "ranger")

### Orden de las funciones

def main():
    health = 10
    armor = 5
    add_armor(health, armor)


def add_armor(h, a):
    new_health = h + a
    print_health(new_health)


def print_health(new_health):
    print(f"The player now has {new_health} health")


# call entrypoint at the end
main()

### entrevista con Boots
# ¡Ha llegado el momento de tu primera lección para la entrevista en Boots !

# En estas lecciones, ¡Boots se convierte en tu entrevistador en lugar de tu tutor! Responde a su pregunta abierta o sigue sus instrucciones. La conversación continuará hasta que esté satisfecho con tus respuestas y cumpla con los criterios de aceptación .

# Trátalo como una entrevista real:

# ¡Puedes hacer preguntas para aclarar dudas sin ninguna penalización (de hecho, se recomienda hacerlo )!
# No tienes que responder de una sola vez, ¡mantén una conversación fluida!
# Boots responderá de una de tres maneras:

# Si haces una pregunta o das una respuesta parcialmente correcta o inconclusa , no hay penalización y Boots te hará una pregunta de seguimiento o aclarará las instrucciones.
# Si dices algo incorrecto o fuera de tema , perderás armadura o tu racha, y Boots intentará redirigirte.
# Una vez que cumpla con los criterios de aceptación , Boots le dará el visto bueno.
# Asignación
# Para responder a la pregunta de Boots, consulte el siguiente fragmento de código:

def calculate_damage(opening_attack, core_damage, finishing_move):
    total = opening_attack + core_damage + finishing_move
    return total


stab_damage = calculate_damage(10, 20, 30)
slash_damage = calculate_damage(5, 10, 15)
fireball_damage = calculate_damage(50, 60, 70)
print(stab_damage)
print(slash_damage)
print(fireball_damage)


def hours_to_seconds(hours):
    return hours * 60 * 60


# Don't touch below this line


def test(hours):
    secs = hours_to_seconds(hours)
    print(hours, "hours is", secs, "seconds")


test(10)
test(1)
test(25)
test(100)
test(33)

# Múltiples valores de retorno
# Una función puede devolver más de un valor separándolos con comas.

def cast_iceblast(wizard_level, start_mana):
    damage = wizard_level * 2
    new_mana = start_mana - 10
    return damage, new_mana  # return two values
damage, mana = cast_iceblast(5, 100)
print(f"Damage: {damage}, Remaining Mana: {mana}")
# Damage: 10, Remaining Mana: 90

#Cuando cast_iceblastse llama a la función, los valores devueltos damagese new_manaasignan a damagey mana, respectivamente. Al igual que con las entradas de la función, lo que importa es el orden de los valores, no los nombres de las variables. Podríamos haber llamado a las variables oney two:

# Assignment
# Complete the become_warrior function. It accepts 2 inputs:

# The full_name string
# The power integer
# It should return 2 values:

# A title string
# A new_power integer.
# Create the title using f-strings. F-strings can be assigned to variables, not just printed. Combine full_name with "the warrior" in this format:
# full_name the warrior

# Be very careful with the output of your program. The text will need to match the expected results exactly. Double-check your spacing and spelling!

# Create the new_power value that is equal to the input power + 1
# Return both title and new_power
# Here's an example of how the function is intended to work:

def become_warrior(full_name, power):
    title= f"{full_name} the warrior"
    new_power= power + 1
    return title,new_power

# Don't edit below this line


def main():
    test("Frodo Baggins", 5)
    test("Bilbo Baggins", 10)
    test("Gandalf The Grey", 9000)


def test(input1, input2):
    result1, result2 = become_warrior(input1, input2)
    print(result1, "has a power level of:", result2)


main()

### Parámetros frente a argumentos
# Los parámetros son los nombres que se utilizan para las entradas al definir una función. Los argumentos son los valores de las entradas que se proporcionan cuando se llama a una función .

# Para reiterar, los argumentos son los valores reales que se introducen en la función, como 42.0, "the dark knight", o True. Los parámetros son los nombres que usamos en la definición de la función para referirnos a esos valores, que en el momento de escribir la función, pueden ser cualquiera que queramos.

# Dicho esto, todo esto es cuestión de semántica, y francamente, los desarrolladores son bastante negligentes con estas definiciones. A menudo se oyen los términos "argumentos" y "parámetros" usados ​​indistintamente.

# a y b are parametros
def add(a, b):
    return a + b


# 5 y 6 are argumentos
sum = add(5, 6)

##------------------cambios alu-------------------##

#Valores predeterminados
# Puedes especificar un valor predeterminado para un parámetro de función, lo cual es útil cuando una función tiene parámetros "opcionales". Estos se crean utilizando el =operador de asignación ( ) dentro de la firma de la función:

def get_greeting(email, name="goofy"):
    print(f"Hello {name}, welcome! You've registered your email: {email}")

# Si la llamamos con ambos parámetros, utiliza los valores proporcionados:

get_greeting("lane@example.com", "Lane")
# Hello Lane, welcome! You've registered your email: lane@example.com

get_greeting("lane@example.com")
# Hello there, welcome! You've registered your email: lane@example.com

# Assignment
# Complete the get_punched and get_slashed functions. They both take two integers as arguments, health and armor.

# Complete the get_punched function:
# In the function signature, give the armor parameter a default value of 0.
# Create a damage variable equal to 50 minus the armor. (Armor lowers the damage).
# Return the result of the input health minus the calculated damage.
# Complete the get_slashed function:
# In the function signature, give the armor parameter a default value of 0.
# Create a damage variable equal to 100 minus the armor.
# Return the result of the input health minus the calculated damage.

def get_punched(health, armor=0):
    damage= 50 - armor
    return health - damage


def get_slashed(health, armor=0):
    damage=100 - armor
    return health - damage


# Don't touch below this line


def test(health, armor):
    print(f"Running tests for health {health} and armor {armor}")
    print("========================================")
    print(f"Health: {health}, Armor: {armor}")
    print(f"Health after punch: {get_punched(health, armor)}")
    print("----------------------------------------")
    print(f"Health: {health}, Armor: {armor}")
    print(f"Health after slash: {get_slashed(health, armor)}")
    print("----------------------------------------")
    print(f"Health: {health}, Armor: no armor!")
    print(f"Health after slash: {get_slashed(health)}")
    print("----------------------------------------")
    print(f"Health: {health}, Armor: no armor!")
    print(f"Health after punch: {get_punched(health)}")
    print("----------------------------------------\n")


test(400, 5)
test(300, 3)
test(200, 1)


# Enchant and Attack
# In Fantasy Quest, a weapon can be enchanted to do bonus damage.

# Assignment
# Complete the enchant_and_attack function. It creates a new "enchanted" name for a weapon and calculates how much damage the enchanted weapon will deal to a targeted enemy.

# It accepts 3 parameters:

# target_health: integer
# damage: integer
# weapon: string
# It should do the following things in the function body:

# Calculate and store the "enchanted damage" in a new variable. The enchanted damage should be the input damage plus 10.
# Calculate and store the "new health" in a new variable. The new health should be the input target_health minus the enchanted damage.
# Create a new variable called enchanted_weapon. It should be the input weapon with the string "enchanted " added to the beginning of it. For example:
# sword -> enchanted sword
# axe -> enchanted axe
# Return the enchanted weapon and the new health in that order.

def enchant_and_attack(target_health, damage, weapon):
    skill = "enchanted"
    enchanted= damage + 10
    new_health = target_health - enchanted
    enchanted_weapon= f"{skill} {weapon}"
    return enchanted_weapon,new_health
    


# Don't modify below this line


def test(target_health, damage, weapon):
    print(f"The target has {target_health} health.")
    print(f"{weapon} base damage: {damage}... Enchanting and attacking.")
    enchanted_weapon, new_health = enchant_and_attack(target_health, damage, weapon)
    print(f"The target has been attacked with the {enchanted_weapon}.")
    print(f"The target has {new_health} health remaining.")
    print("=====================================")


def main():
    test(100, 50, "sword")
    test(500, 100, "axe")
    test(1000, 250, "bow")


main()
