## list ##
# Una forma natural de organizar y almacenar datos es mediante listas List. Algunos lenguajes las llaman "arrays", pero en Python simplemente las llamamos listas. Piensa en todas las aplicaciones que usas y en cuántos de sus elementos están organizados en listas.
# Listas (continuación)
# A veces, al crear listas manualmente, puede resultar difícil leerlas si todos los elementos están en la misma línea de código. Podemos declarar la lista usando varias líneas si queremos:

flower_types = [
    "daffodil",
    "rose",
    "chrysanthemum",
]

player_ages = [
    23,
    18,
    31,
    42,
]

# Longitud de la lista
# La longitud de una lista se puede calcular utilizando la len()función. Esta función recibe un iterable (como una cadena o una lista) y devuelve el número de elementos presentes.

fruits = ["apple", "banana", "pear"]
length = len(fruits)
# 3 items in fruits

len("supercalifragilisticexpialidocious")
# 34 characters

# No te dejes engañar por el hecho de que la longitud no sea igual al índice del último elemento. De hecho, siempre será una unidad mayor, ¡porque el índice inicial es cero!
# Completa la get_last_indexfunción para que devuelva la longitud de la inventorylista menos 1.
# def get_last_index(inventory):
#     return len(inventory) - 1 

# Agregar contenido en Python
# Es común crear una lista vacía y luego llenarla con valores usando un bucle. Podemos agregar valores al final de una lista usando el .append()método:
"""
Valores pop
.pop()es lo opuesto a .append(). Pop elimina el último elemento de una lista y lo devuelve para su uso. Por ejemplo:
"""
vegetables = ["broccoli", "cabbage", "kale", "tomato"]
last_vegetable = vegetables.pop()
# vegetables = ['broccoli', 'cabbage', 'kale']
# last_vegetable = 'tomato'

def clear_inventory():
    inventory = [
        "Healing Potion",
        "Iron Bar",
        "Kite Shield",
        "Shortsword",
        "Leather Scraps",
        "Tattered Cloth",
    ]

    print(f"inventory: {inventory}")

    # don't touch above this line

    for i in range(0, len(inventory)):
        # ?
        item = inventory.pop()
        # don't touch below this line
        print(f"Selling: {item}")
        print(f"inventory: {inventory}")


def test():
    clear_inventory()
    print("=====================================")


def main():
    test()


main()

# Sintaxis sin índice
# En mi opinión, Python tiene la sintaxis más elegante para iterar directamente sobre los elementos de una lista sin preocuparse por los índices. Si no necesitas el índice, puedes usar la siguiente sintaxis:

trees = ["oak", "pine", "maple"]
for tree in trees:
    print(tree)

# Prints:
# oak
# pine
# maple
"""
Si no necesitamos actualizar el elemento y solo acceder a su valor, esta es una forma más limpia de escribir el código.
"""

# def contains_leather_scraps(items):
#     for item in items:
#         if item == "Leather Scraps":
#             return True
#     return False

"""
Encuentra a Max
Infinidad
La función integrada float() puede crear un valor numérico de punto flotante de infinito negativo. En lugar de inicializar un valor base como 0o -100000, podemos usar float("-inf")para representar infinito negativo. Dado que cada valor será mayor que infinito negativo, podemos usarlo como punto de partida para ayudarnos a lograr nuestro objetivo de encontrar el valor máximo.
"""

negative_infinity = float("-inf")
positive_infinity = float("inf")
"""
Asignación
Nuestros jugadores quieren ver el ataque más potente de su último combate. Algunos enemigos pueden recibir mejoras que les permiten absorber ataques mágicos o cuerpo a cuerpo como si fueran salud, lo que resulta en daño negativo. Añadamos otra función para analizar los datos del registro de combate.

Completa la find_maxfunción. Recibe como entrada una lista de números enteros numsy devuelve un número.

max_so_farse inicializa como infinito negativo.
Compara cada número de numscon max_so_far. Si algún número es mayor que max_so_far, reemplázalo max_so_farcon ese valor.
Después de iterar sobre cada número, devuelve max_so_far. Si numsestá vacío, devuelve infinito negativo.
Aquí tienes un ejemplo de cómo find_maxdebería funcionar tu función cuando se la llame:
"""

def find_max(nums):
    negative_infinity = float("-inf")
    if len(nums) == 0:
        return negative_infinity

    max_so_far = float("-inf")
    for num in nums:
        if num > max_so_far:
            max_so_far = num
             
    return max_so_far

print(find_max([100, 10, 22]))

# Encuentra el resto:
# El operador módulo se puede usar para encontrar el resto después de una división. Por ejemplo, 7 el módulo 2 sería 1, porque 2 se puede multiplicar exactamente por 7 como máximo 3 veces:

# 2 * 3 = 6

# Entonces queda 1 para llegar de 6 a 7.

# 7 - 6 = 1

# El operador módulo es el signo de porcentaje: %.  ¡Es importante tener en cuenta que módulo no es un porcentaje!


# Segmentación de listas
# Python facilita la segmentación de listas para trabajar solo con la sección que te interesa. Una forma de hacerlo es usar el operador de segmentación simple, que es simplemente dos puntos :.

# Con este operador, puede especificar dónde comenzar y terminar la segmentación, y cómo recorrer la lista original. La segmentación de listas devuelve una nueva lista a partir de la lista existente.

# La sintaxis es la siguiente:

# my_list[start:stop:step]

scores = [50, 70, 30, 20, 90, 10, 50]
# Display list
print(scores[1:5:2])
# Prints [70, 20]
# Lo anterior utiliza un start de 1, un stop de 5(no incluido) y un step de 2. Todas las secciones son opcionales .
# Python: Slicing de Listas (List Slicing)
"""
Sintaxis general:
`lista[inicio : fin : paso]`
- **`inicio`**: Incluido (por defecto: `0`).
- **`fin`**: Excluido (por defecto: longitud de la lista).
- **`paso`**: Salto entre elementos (por defecto: `1`).

---

## 1. Omitir secciones

- **Desde el inicio hasta el índice N (exclusivo):**
  ```python
  numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  numbers[:3]  # [0, 1, 2]
"""
# #Desde el índice N hasta el final:
# numbers[3:]  # [3, 4, 5, 6, 7, 8, 9]
# #Usar solo el "paso" (stride)
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# numbers[::2]  # Elementos en índices pares: [0, 2, 4, 6, 8]

# 3. Índices negativos
# Cuentan desde el final hacia atrás (-1 es el último elemento):

# Python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Últimos 3 elementos:
numbers[-3:]  # [7, 8, 9]

# Todos excepto el último:
numbers[:-1]  # [0, 1, 2, 3, 4, 5, 6, 7, 8]
"""
Asignación
Completa la get_champion_slicesfunción dada. Recibe una lista de championsy debe devolver tres nuevas listas basadas en los campeones dados:

Primero, devuelve una parte de la championslista que comience con el tercer campeón y llegue hasta el final de la lista.
A continuación, devuelve una parte de la championslista que comience al principio de la misma e incluya a todos los campeones excepto al último.
Por último, devuelve una porción de la championslista que solo incluya a los campeones en índices pares (0, 2, 4, ...).
"""
def get_champion_slices(champions):
    return champions[2:],champions[:len(champions)-1],champions[::2]

print(get_champion_slices(["Aatrox", "Ahri", "Akali", "Alistar", "Amumu"]))

# Operaciones de lista – Contiene
# Comprobar si un valor existe en una lista o no también es muy fácil en Python: simplemente use la inpalabra clave para comprobar su presencia o not insu ausencia.

fruits = ["apple", "orange", "banana"]
print("banana" in fruits)
# Prints: True

fruits = ["apple", "orange", "banana"]
print("banana" not in fruits)
# Prints: False

# Eliminación de lista
# Python cuenta con una palabra clave integrada , `del`, que permite eliminar elementos de los objetos. En el caso de una lista, se pueden eliminar índices específicos o segmentos completos.

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# delete the fourth item
del nums[3]
print(nums)
# Output: [1, 2, 3, 5, 6, 7, 8, 9]

# delete the second item up to (but not including) the fourth item
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del nums[1:3]
print(nums)
# Output: [1, 4, 5, 6, 7, 8, 9]

# delete all elements
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del nums[:]
print(nums)
"""
ssignment
In Fantasy Quest there is a list of strongholds on the map that players can visit to defeat powerful bosses. Let's update the trim_strongholds function to:

Delete the first stronghold from the list
Delete the last two strongholds from the list
"""

def trim_strongholds(strongholds):
    del strongholds[0]
    del strongholds[-2:]

    return strongholds

print(trim_strongholds(["Dragon's Lair", "Goblin's Den", "Troll's Bridge", "Witch's Hut", "Vampire's Castle"]))

# Tuplas
# Las tuplas son colecciones de datos ordenadas e inmutables. Puedes pensar en una tupla como Listuna lista de tamaño fijo. Las tuplas se crean con paréntesis:

my_tuple = ("this is a tuple", 45, True)
print(my_tuple[0])
# this is a tuple
print(my_tuple[1])
# 45
print(my_tuple[2])
# True

# Las tuplas se utilizan a menudo para almacenar grupos muy pequeños de datos (como 2 o 3 elementos). Por ejemplo, se podría usar una tupla para almacenar el nombre y la edad de un perro.

dog = ("Fido", 4)

#Existe un caso especial para crear tuplas de un solo elemento. Debes incluir una coma para que Python sepa que es una tupla y no paréntesis normales:

dog = ("Fido",)
# Desempaquetado de tuplas
# Puedes asignar fácilmente los valores de una tupla a variables mediante el desempaquetado.

dog = ("Fido", 4)
dog_name, dog_age = dog
print(dog_name)
# Fido
print(dog_age)
# 4

# Lista inversa
# Asignación
# Algunos de nuestros jugadores quisieran ver sus inventarios en orden inverso.

# Usando un bucle, vamos a escribir una función que tome una lista como entrada y devuelva una nueva lista, pero con todos los elementos en orden inverso.

def reverse_list(items):
    invert = []
    for i in range(len(items) - 1,-1,-1):
        invert.append(items[i])

    return invert

print(reverse_list(["Healing Potion", "Iron Bar", "Kite Shield", "Shortsword", "Leather Scraps", "Tattered Cloth"]))

"""
1. len(items) - 1 # (el comienzo)
Las listas tienen índice cero, lo que significa que el primer elemento está en el índice 0 y el último en el índice len(items) - 1. Si tu lista tiene 5 elementos, los índices válidos son 0, 1, 2, 3, 4, no 5. Por lo tanto, para comenzar en el último elemento, necesitas len(items) - 1.
"""
items = ["a", "b", "c", "d", "e"]
len(items) # 5
len(items) - 1 # 4, which is the index of "e"
"""
2. -1(la parada)

Esto indica rangedónde detenerse, pero rangesiempre se detiene antes de alcanzar este valor. Dado que deseas que tu bucle incluya el índice 0, necesitas que el valor de parada sea uno menos que 0, que es -1. Si usaras 0como valor de parada, el bucle se detendría antes de 0, omitiendo el primer elemento por completo.

3. -1(el paso)

Esto es cuánto icambia en cada iteración. Un paso -1significa "disminuir en 1 cada vez" en lugar del comportamiento de aumento predeterminado. Así que iva de 4, 3, 2, 1, 0 en lugar de contar hacia arriba.

En conjunto: range(4, -1, -1)produce 4, 3, 2, 1, 0exactamente los índices necesarios para recorrer la lista hacia atrás.
"""
# Lección: Filtrar Mensajes (Filter Messages)
# Estás a punto de escribir un poco más de código en una sola función de lo que has hecho hasta ahora.

# Consejo de depuración (Debugging): No intentes escribirlo todo de una vez. Empieza por el bucle exterior y ve avanzando hacia el interior. Añade instrucciones print() adicionales y ejecuta el código con frecuencia para asegurarte de que cada línea funciona como esperas. Todos los programadores profesionales dividen los problemas grandes en partes pequeñas. (Recuerda eliminar los print() adicionales antes de entregar tu código).

# Herramientas Clave de Python
# Dado que trabajaremos convirtiendo cadenas de texto (strings) en listas (lists) y viceversa, estos dos métodos nos facilitarán mucho la vida:

# 1. Dividir una cadena en una lista: .split()
# Se aplica a una cadena de texto y devuelve una lista dividiendo el texto según un delimitador. Si no le pasas ningún argumento entre los paréntesis, dividirá la cadena automáticamente por los espacios en blanco.
# Python
message = "hello there sam"
words = message.split()
print(words)
# Imprime: ['hello', 'there', 'sam']

# 2. Unir una lista en una sola cadena: .join()
# Se llama sobre el delimitador (el texto que quieres poner entre cada palabra, como un espacio " ") y recibe como argumento la lista de palabras que quieres unir.

# Python
list_of_words = ["hello", "there", "sam"]
sentence = " ".join(list_of_words)
print(sentence)
# Imprime: hello there sam

"""
Asignación
¡Necesitamos filtrar las palabrotas del chat en vivo de nuestro juego! Completa la filter_messagesfunción. Recibe como entrada una lista de mensajes de chat y devuelve dos listas nuevas:

Una lista con los mismos mensajes, pero sin ninguna mención de la palabra dang.
Una lista que contiene el número de dangpalabras que se eliminaron de cada mensaje en ese índice en particular.
Aquí hay algunos ejemplos:
"""
# Aquí tienes los pasos que debes seguir. ¡Son MUCHOS pasos! No será fácil, pero si sigues los pasos al pie de la letra , aprobarás esta tarea.

# Crea las dos listas vacías que devolverás al final:
# Uno para los mensajes filtrados con "dang"eliminados.
# Y uno por la cantidad de "dangs" eliminados de esos mensajes.
# Recorre la lista de mensajes. Para cada mensaje:
# Divide la cadena del mensaje en una lista de palabras utilizando el .split()método de cadena.
# Crea una lista vacía con todas las palabras buenas de este mensaje.
# Crea una variable de contador para los "dangs" en este mensaje, comenzando en 0.
# Por cada palabra del mensaje:
# Si la palabra es "dang", agréguela 1al contador de "dangs".
# Si la palabra no "dang" es , agrégala a la lista de buenas palabras.
# Une la lista de buenas palabras en una sola cadena usando el .join()método.
# Agregue el nuevo mensaje filtrado a la lista de mensajes filtrados.
# Añade el nuevo recuento de "dangs" a la lista de recuentos de "dangs".
# Después de recorrer la lista de mensajes, devuelva primero la lista de mensajes filtrados y luego la lista de recuentos de "dang".

def filter_messages(messages):
    filtered_messages = []
    dang_counts = []

    for message in messages:
        words = message.split()
        good_words = []
        dangs = 0

        for word in words:
            if word == "dang":
                dangs += 1
            else:
                good_words.append(word)

        sentence = " ".join(good_words)
        filtered_messages.append(sentence)
        dang_counts.append(dangs)

    return filtered_messages, dang_counts
        
        
print(filter_messages(["dang it", "dang dang", "dang it again", "no dang here"]))
