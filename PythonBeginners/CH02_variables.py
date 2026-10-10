player_health = 1000

# reduce by 100 here
player_health = 900
print(player_health)

# and here
player_health = 800
print(player_health)

# and here
player_health = 700
print(player_health)

# and here
player_health = 600
print(player_health)

#***************************************************#

player_health = 1000
armor_multiplier = 2
armored_health = player_health * armor_multiplier

print(armored_health)

# Comentario de una sola línea
# Un solo verso #convierte el resto de la línea en un comentario:

# # speed describes how fast the player
# # moves in meters per second

"""
Nombre	Descripción	Código	Idioma(s) que lo recomiendan
Caso de serpiente	Todas las palabras están en minúsculas y separadas por guiones bajos.	
num_new_users	Python, Ruby, Rust
"""

#Dicho esto, se prefieren las comillas dobles .

player_health = 100

player_has_magic = True

# don't touch below this line
print("player_health is a/an", type(player_health).__name__)
print("player_has_magic is a/an", type(player_has_magic).__name__)

# Cadenas F en Python
# ¿Alguna vez has jugado al Pokémon clásico y has elegido un nombre gracioso para que los mensajes del juego resultaran divertidos?

#Agregue un f al principio de las comillas para crear una cadena f:f"this is easy!"
# Utilice llaves {}alrededor de una variable para interpolar (insertar) su valor en la cadena.


# create the empty "enemy" variable here
enemy = None

# don't touch below this line
print(enemy is None)

# Tipografía dinámica
# Python es de tipado dinámico , lo que significa que una variable puede almacenar cualquier tipo, y ese tipo puede cambiar .

# Por ejemplo, si creo una variable numérica, posteriormente puedo cambiar esa variable a una cadena de texto:

speed = 5
speed = "five"

print(speed)

# Pero, bueno, tal vez no.
# En casi todas las circunstancias, es una mala idea cambiar el tipo de una variable. Lo "correcto" es simplemente crear una nueva. Por ejemplo:

speed = 5
speed_description = "five"


"""
¿Qué es la tipificación no dinámica?
Los lenguajes que no son de tipado dinámico son de tipado estático , 
omo Go y TypeScript (uno de los cuales aprenderás en un curso posterior, 
dependiendo de la especialización que elijas). En un lenguaje de tipado estático
, si intentas asignar un valor a una variable de tipo incorrecto, obtendrás un 
error de compilación y el programa no se ejecutará.

Si Python fuera de tipado estático, el primer ejemplo anterior no permitiría 
la segunda línea, speed = "five". El ordenador daría un error del tipo you can't
 assign a string value ("five") to a number variable (speed).
"""

# Matemáticas con cadenas de caracteres
# Al trabajar con cadenas, el +operador realiza una " concatenación ", que es una palabra elegante que significa "unir dos cadenas". En general, es mejor usar la interpolación de cadenas en f-stringslugar de +la concatenación .

#ejemplo 
sentence_start = "You have "
sentence_end = " health"

player1_health = "1200"
player2_health = "1100"

# Don't edit above this line

print(sentence_start + player1_health + sentence_end)
print(sentence_start + player2_health + sentence_end)


# Declaración multivariable
# Podemos ahorrar espacio al crear muchas variables nuevas declarándolas en la misma línea:

sword_name, sword_damage, sword_length = "Excalibur", 10, 200


# Lo cual es lo mismo que:

sword_name = "Excalibur"
sword_damage = 10
sword_length = 200

## Botas ##

# Quizás ya lo hayas adivinado, pero debajo de la explicación de la lección, hay un adorable oso mago llamado Botas . Su trabajo es ayudarte si te quedas atascado.

# Boots es un chatbot de IA (como ChatGPT) que tiene acceso a tu lección. Cuando le haces una pregunta, él ya sabe:
# La solución oficial
# Lo que te han pedido que hagas
# Cambios que has realizado en el código
# Ha sido entrenado para no darte la respuesta. Utiliza el método socrático para simplemente orientarte en la dirección correcta.
# Iniciar una conversación con Boots antes de completar una lección cuesta 1 salmón al horno (es un tipo hambriento) o, si no tienes uno, el 50% de la XP de la lección.
# Solo para esta lección, podrás conseguir suficientes gemas para comprar un salmón al horno .
# Conversar con Boots después de completar una lección es gratuito y se recomienda para profundizar en tu comprensión .

"""

El método socrático es una forma de diálogo argumentativo en la que un individuo interroga a su interlocutor sobre un tema, mediante preguntas y aclaraciones, hasta que este se ve obligado a llegar a una conclusión por sí mismo, o bien su razonamiento se desmorona y se ve forzado a admitir su ignorancia.
"""
player_name = "Charles"
greeting = "Well met,"
quest_start = "The local mine has been taken over by orcs!"
quest_end = "We need your help taking it back."
space = " "

# don't touch above this line

complete_greeting = greeting + space + player_name
print(complete_greeting)
print(quest_start)
print(quest_end)



