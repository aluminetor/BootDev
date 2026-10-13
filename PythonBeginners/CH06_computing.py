### COMPUTING

# Números de Python
# En Python, los números sin punto decimal se llaman Integersde la misma manera que en matemáticas.

# Los números enteros son simplemente números naturales, positivos o negativos. Por ejemplo, 3y -3son ejemplos de números enteros.

def calculate_damage(sword, arrow, spear, dagger, fireball):
    total_damage = sword + arrow + spear + dagger + fireball
    average_damage = total_damage / 5
    return total_damage, average_damage
    
# esto esta en el main_test_py de forma larga
print(calculate_damage(3, 5, 2, 1, 4))

#División de pisos

# Python ofrece un excelente soporte nativo para operaciones matemáticas. Esto, entre otras razones, explica su gran éxito en aplicaciones de inteligencia artificial, aprendizaje automático y ciencia de datos.

# La división entera es como la división normal, excepto que el resultado se redondea hacia abajo al entero más cercano. El //operador se utiliza para la división entera.
print(11 // 2)
# 2 (an integer, rounded down from 2.666)
print(-7 // 3)
# -3 (an integer, rounded down from -2.333)

"""
Exponentes
Python tiene soporte integrado para exponentes, algo para lo que la mayoría de los lenguajes requieren una mathbiblioteca.

# reads as "three squared" or
# "three raised to the second power"

"""
print(3**2)
# 9

# Más es igual a
# Python facilita la reasignación al realizar operaciones matemáticas. En JavaScript o Go, es posible que estés familiarizado con la ++sintaxis para incrementar una variable numérica en 1. En Python, utilizamos el += operador de incremento in situ .

star_rating = 4
star_rating +=1
print(star_rating)

#Notacion cientifica

print(16e3)

print(7.1e-2)

"""
En resumen, el exponente que sigue a la coma decimal e especifica cuántas posiciones se debe mover la coma decimal: a la derecha cuando el exponente es positivo y a la izquierda cuando es negativo.
"""
num = 16_000_000
print(num)
# Prints 16000000

# Asignación
# Debido a las limitaciones del servidor de nuestra aplicación, existe un número máximo de jugadores que podemos tener en un único servidor de Fantasy Quest.

# Completa la max_players_on_serverfunción. No requiere ninguna entrada, simplemente devuelve 3 números estáticos:

# Número máximo de jugadores en un servidor "pequeño": 1,024,000,000,000,000,000( 1.024e18)
# Número máximo de jugadores en un servidor "medio":10,240,000,000,000,000,000
# Número máximo de jugadores en un servidor "grande":102,400,000,000,000,000,000
# Utilice la notación científica para representar estos números. Por ejemplo: 3.104e15.


def max_players_on_server():
    small_server = 1.024e18
    medium_server = 1.024e19
    large_server = 1.024e20
    return small_server, medium_server, large_server

# Operadores lógicos
# Probablemente estés familiarizado con los operadores lógicos andy or.

# Los operadores lógicos trabajan con valores booleanos , Truey False.

# El operador lógico andrequiere que ambas entradas Truedevuelvan True. El oroperador lógico solo requiere que al menos una entrada Truedevuelva True.

# Por ejemplo:
print(True and True)
# prints True

print(True or False)
# prints True

print((True or False) and False)
print(((True and True) or (True and False)))

# No
# Nos saltamos un operador lógico muy importante: not. Este notoperador invierte el resultado. Devuelve Falsesi la entrada fue Truey viceversa.

print(not True)
# Prints: False

print(not False)
# Prints: True

"""
Números binarios
Los números binarios son simplemente números en base 2. Funcionan de la misma manera que los números normales en base 10, pero con dos símbolos en lugar de diez.

Símbolos de base 2 (binarios): 0y1
Símbolos de base 10 (decimal): 0, 1, 2, 3, 4, 5, 6, 7, 8,9
"""
## es mi forma para convertir numeros decimales a binarios
def decimal_binario(num):
    residuo = 0
    cociente = num
    binario = ""
    
    if num < 1:
        return 0
    
    while cociente >= 1:
        cociente,residuo = cociente // 2, cociente % 2
        binario = str(residuo) + binario

    return int(binario)

print(decimal_binario(13))

# El valor posicional de cada dígito es el doble del valor posicional a su derecha. En un número binario de 4 dígitos, los valores posicionales son:

# Ocho
# Cuatro
# Dos años
# Unos
# Por ejemplo, 0101significa:

# 0ochos
# 1cuatro
# 0dos
# 1uno
# Así 0101es 5en decimal.

# Intenta cambiar los bits:

# Convertidor binario
# Haz clic en los bits para invertirlos y ver el valor decimal equivalente.
"""
El video ilustra cómo funciona el sistema de numeración binaria (base 2) en comparación con el sistema decimal (base 10) que usamos todos los días.

Aquí tienes un resumen de los puntos clave:

¿Qué es el sistema binario?

El sistema decimal usa 10 dígitos (del 0al 9).
El sistema binario solo usa 2 dígitos: 0y 1(llamados bits ).
Valores posicionales (potencias de 2):

En decimal, cada columna a la izquierda vale 10 veces más (unidades, decenas, centenas, millas: 1, 10, 100, 1000).
En binario, cada columna a la izquierda vale el doble que la anterior. De derecha a izquierda, las posiciones valen:
1
2
4
8
16
32
etc.
Cómo leer y convertir un número binario:

Un 1 significa que sumas el valor de esa posición; un 0 significado que lo ignora.
Por ejemplo, el número binario 1101:
Posición del 8: 1-> suma 8
Posición del 4: 1-> suma 4
Posición del 2: 0-> suma 0
Posición del 1: 1-> suma 1
Total: 8 + 4 + 0 + 1 = 13 en decimal.
Por qué lo usan las computadoras:

A nivel de hardware, los circuitos y transistores funcionan con electricidad: pueden estar apagados ( 0) o encendidos ( 1). Por eso, toda la información en una computadora se representa internamente mediante secuencias de ceros y unos
"""

# Operador bit a bit “&”
# Los operadores bit a bit son similares a los operadores lógicos, pero en lugar de operar sobre valores booleanos, aplican la misma lógica a todos los bits de un valor por columna. Por ejemplo, supongamos que tiene los números 5y 7representados en binario . Podría realizar una operación AND bit a bit y el resultado sería 5.

# 0101 es 5
# 0111 es 7

0b0101 & 0b0111
# equals 5

binary_five = 0b0101
binary_seven = 0b0111
binary_five & binary_seven
# equals 5

"""
Permisos del gremio
A veces, las aplicaciones almacenan los permisos de usuario como valores binarios. Si 4un usuario puede tener diferentes permisos, puedo almacenarlos como un número binario de cuatro dígitos. Si un bit específico está presente, sé que el permiso está habilitado. Esto puede ser mucho más eficiente que almacenar cadenas de texto completas.

Imaginemos que tenemos 4 permisos relacionados con los "gremios" en Fantasy Quest ("gremio" es simplemente una palabra elegante de videojuego para "equipo"):

can_create_guild– Bit más a la izquierda ( 0b1000)
can_review_guild– El segundo bit más a la izquierda ( 0b0100)
can_delete_guild– El segundo bit más a la derecha ( 0b0010)
can_edit_guild– Bit más a la derecha ( 0b0001)
Si un usuario no tiene permisos, sus permisos binarios serían 0b0000.

Si un usuario solo tiene el can_create_guildpermiso, sus permisos binarios serían 0b1000, pero un usuario con permisos can_review_guild y can_edit_guild serían 0b0101.

Para comprobar, por ejemplo, el can_review_guildpermiso, podemos realizar una operación AND bit a bit entre los permisos del usuario y el can_review_guildbit habilitado ( 0b0100). Si el resultado es 0b0100nuevamente, ¡sabemos que tiene ese permiso específico!

user_permissions = 0b0101
can_review_guild = 0b0100

# perform bitwise AND to get the user's review permission
user_review_guild_permission = user_permissions & can_review_guild

# check if the user's review permission is equal to `can_review_guild`

Asignación
Completa cada una de las get_XXX_bitsfunciones. Simplemente usa la &operación bit a bit en la entrada de los bits de permiso del usuario y la variable de bits de permiso del gremio correspondiente, y devuelve los bits resultantes para que las pruebas los verifiquen.

Se han proporcionado 4 valores; utilice el adecuado para cada función:

can_create_guild
can_review_guild
can_delete_guild
can_edit_guild
"""


# El tema principal es el uso del operador bit a bit & (Bitwise AND) como máscara de bits (bitmask) para gestionar y consultar permisos de forma ultra eficiente.

# 1. ¿Cómo funciona el operador &?
# Compara dos números en binario columna por columna (bit a bit). El resultado solo es 1 si ambos bits comparados son 1; en cualquier otro caso es 0:

can_create_guild = 0b1000
can_review_guild = 0b0100
can_delete_guild = 0b0010
can_edit_guild = 0b0001


def get_create_bits(user_permissions):
    return user_permissions & can_create_guild


def get_review_bits(user_permissions):
    return user_permissions & can_review_guild



def get_delete_bits(user_permissions):
    return user_permissions & can_delete_guild



def get_edit_bits(user_permissions):
    return user_permissions & can_edit_guild


usuario = 0b0101  # Tiene Revisar (0100) y Editar (0001)

# ¿Tiene permiso de Revisar?
resultado = usuario & 0b0100  # 0b0101 & 0b0100 = 0b0100
# Como el resultado coincide con 0b0100 (distinto de 0), SÍ lo tiene.

# ¿Tiene permiso de Crear?
resultado = usuario & 0b1000  # 0b0101 & 0b1000 = 0b0000
# Como el resultado es 0b0000 (0), NO lo tiene.

# Operador bit a bit “|”
# Como habrás adivinado, el operador "o" bit a bit es similar al operador "y" bit a bit, ya que funciona con valores binarios en lugar de booleanos. Sin embargo, el operador "o" bit a bit combina los bits. Aquí tienes un ejemplo:

# 0101 es 5
# 0111 es 7

"""
0101
|
0111
=
0111
"""
#Usa el delimitador de miles adecuado para que los números sigan siendo fáciles de interpretar visualmente.
def main():
    calculate_dps(8_000_000, 45)
    calculate_dps(10_000_000, 49)


# Don't edit below this line


def calculate_dps(damage, time):
    dps = damage / time
    print(f"Damage per second: {dps}")
    print("=====================================")

main()

# Conversión binaria
# Fantasy Quest necesita migrar datos antiguos de cadenas que parecen binarias a los números enteros que representan dichas cadenas binarias. Por ejemplo:

# "100" -> 4
# "101" -> 5
# "10010" -> 18
# La función integrada int() puede convertir una cadena binaria en un número entero. Recibe un segundo argumento que especifica la base del número (binario es base 2). Por ejemplo:

# this is a binary string
binary_string = "100"

# convert binary string to integer
num = int(binary_string, 2)
print(num)
# 4

def binary_string_to_int(num_servers, num_players, num_admins):
    return int(num_servers, 2), int(num_players, 2),int(num_admins, 2)