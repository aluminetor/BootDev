"""

Diccionarios
En Python, los diccionarios se utilizan para almacenar valores de datos en pares keyclave- valuevalor. Son una excelente manera de almacenar grupos de información.
"""
# use curly braces
# add key-value pairs
car = {
    "brand": "Toyota",
    "model": "Camry",
    "year": 2019,
}



# Aquí la carvariable se asigna a un diccionario {}que contiene las claves brand, modely year. Los valores correspondientes de las claves son Toyota, Camryy 2019.


# Asignación
# Completa la get_character_recordfunción. Recibe como entradas individuales los caracteres name, server, level, y rank, y devuelve un diccionario con las siguientes claves de cadena:

# "name"
# "server"
# "level"
# "rank"
# "id"
# Crea y devuelve un diccionario con las claves anteriores.

# Asigne cada una de las cuatro entradas a la clave correspondiente, es decir, "name": name.

# A continuación, ¡no queremos dos personajes con el mismo nombre bloodwarrior123en el mismo servidor!

# Para la quinta clave, idcree un valor único de la siguiente manera:

# Utilice una f-string para concatenar las entradas namey con una en el medio. Por ejemplo, dado:server#

# nombre = "bloodwarrior123"
# servidor = "servidor1"
# Entonces el idcampo se establecería en bloodwarrior123#server1.

def get_character_record(name, server, level, rank):
    
    return {
        "name": name,
        "server": server,
        "level": level,
        "rank": rank,
        "id": f"{name}#{server}"
    }
    

print(get_character_record("bloodwarrior123", "server1", 50, "Champion"))

# Claves duplicadas
# Dado que los diccionarios dependen de claves únicas, no se pueden tener dos claves iguales en el mismo diccionario. Si intentas usar la misma clave dos veces, el primer valor simplemente se sobrescribirá.

# Acceso a los valores del diccionario
# Los elementos del diccionario deben ser accesibles de alguna manera en el código; de lo contrario, no serían muy útiles.

# Se recupera un valor de un diccionario especificando su clave correspondiente entre corchetes. Los corchetes se parecen a la indexación de una lista.

car = {"make": "Toyota", "model": "Camry"}
print(car["make"])
print(car["model"])
# Prints: Toyota

# Configuración de valores del diccionario
# No es necesario crear un diccionario con valores predefinidos. Es común crear un diccionario vacío y luego rellenarlo con valores dinámicos. La sintaxis es la misma que para obtener datos de una clave; simplemente usa el operador de asignación ( =) para asignarle un valor.

planets = {}
planets["Earth"] = True
planets["Pluto"] = False
print(planets["Pluto"])
# Prints False

full_names = ["jack bronson", "jill mcarty", "john denver"]

names_dict = {}
for full_name in full_names:
    # .split() returns a list of strings
    # where each string is a single word from the original
    name_parts = full_name.split()

    # here we update the dictionary
    names_dict[name_parts[0]] = name_parts[1]

print(names_dict)
# Prints: {'jack': 'bronson', 'jill': 'mcarty', 'john': 'denver'}

full_names = ["jack bronson", "james mcarty", "jack denver"]

names_dict = {}
for full_name in full_names:
    # .split() returns a list of strings
    # where each string is a single word from the original
    names = full_name.split()
    first_name = names[0]
    last_name = names[1]
    names_dict[first_name] = last_name

print(names_dict)
# {'jack': 'denver', 'james': 'mcarty'}

# Eliminar valores del diccionario
# Puede eliminar las claves existentes utilizando la delpalabra clave.

names_dict = {"jack": "bronson", "jill": "mcarty", "joe": "denver"}

del names_dict["joe"]

print(names_dict)
# Prints: {'jack': 'bronson', 'jill': 'mcarty'}

# Eliminar claves que no existen
# Ten en cuenta que si intentas eliminar una clave que no existe, recibirás un error .

# Comprobando la existencia
# Si no está seguro de si una clave existe en un diccionario, utilice la inpalabra clave.

cars = {"ford": "f150", "toyota": "camry"}

print("ford" in cars)
# Prints: True

print("gmc" in cars)
# Prints: False

# Asignación
# Necesitamos informar cuántos enemigos hay en las inmediaciones de nuestros jugadores, ¡pero ellos quieren saber qué tipo de enemigos son! Corrige la count_enemiesfunción. Acepta como entrada:

# enemy_names: una lista de cadenas
# Debe devolver un diccionario donde:

# Las claves son todos los nombres de los enemigos de la lista.
# Los valores son el número de veces que apareció cada enemigo en la lista.
# Ejecuta el código en su estado actual. Generará un KeyError .
# Corrección del código: antes de actualizar el valor de una clave, compruebe si la clave ya existe en el diccionario. Si existe, incremente su valor. Si no existe, establezca esa clave en un valor nulo para 1crear su primera entrada en el diccionario.


def count_enemies(enemy_names):
    enemies_dict = {}
    for enemy_name in enemy_names:
        if enemy_name in enemies_dict:
            enemies_dict[enemy_name] += 1
        else:
            enemies_dict[enemy_name] = 1
    return enemies_dict

print(count_enemies(["goblin", "goblin", "orc", "goblin", "troll", "orc"]))


# Iterar sobre un diccionario en Python
# Podemos iterar sobre las claves de un diccionario usando la misma sintaxis sin índice que usamos para iterar sobre los valores de una lista. Usa cada clave entre corchetes para obtener su valor.

fruit_sizes = {"apple": "small", "banana": "large", "grape": "tiny"}

for name in fruit_sizes:
    size = fruit_sizes[name]
    print(f"name: {name}, size: {size}")

# name: apple, size: small
# name: banana, size: large
# name: grape, size: tiny

def get_most_common_enemy(enemies_dict):
    max_so_far = float("-inf")
    most_common = None
    for enemy_name in enemies_dict:
        count = enemies_dict[enemy_name]
        if count > max_so_far:
            max_so_far = count
            most_common = enemy_name
    return most_common




print(get_most_common_enemy({"jackal": 2, "gremlin": 7}))
print(get_most_common_enemy({"jackal": 3}))
print(get_most_common_enemy({}))
print(get_most_common_enemy({"kobold": 5, "soldier": 5, "gremlin": 5, "dragon": 5}))
print(get_most_common_enemy({"jackal": 5, "kobold": 3, "soldier": 10, "gremlin": 5, "dragon": 20}))
print(get_most_common_enemy({"jackal": 5, "kobold": 3, "soldier": 2, "gremlin": 10, "dragon": 1}))
            
def get_quest_status(progress):
    return progress["quest"]["bridge_run"]["status"]

print(get_quest_status({"quest": {"bridge_run": {"status": "in_progress"}}}))
print(get_quest_status({"quest": {"bridge_run": {"status": "complete"}}}))

# Asignación
# Completa la mergefunción . Acepta dos diccionarios como entrada y devuelve un nuevo diccionario combinado que contiene todas las claves y valores de los diccionarios de entrada.

# Existen varias soluciones que utilizan funciones integradas de Python, pero para practicar solo usaremos bucles:

# Crea un diccionario vacío para almacenar el nuevo resultado combinado.
# Itera sobre los pares clave/valor de dict1 y agrégalos al diccionario combinado.
# Itera sobre los pares clave/valor de dict2 y agrégalos al diccionario combinado.
# Devuelve el diccionario recién fusionado.
# Si una clave existe en ambos diccionarios, el valor del segundo diccionario debe sobrescribir el valor del primero. Aquí tienes un ejemplo de uso:

def merge(dict1, dict2):
    # implement this
    new_merge = {}


# After merge is implemented:
two_towers = {"Frodo": 56, "Aragorn": 10}
rotk = {"Aragorn": 100, "Gandalf": 809}
merged_dict = merge(two_towers, rotk)
print(merged_dict)
# Output: {'Frodo': 56, 'Aragorn': 100, 'Gandalf': 809}

# Observa cómo se actualizó el valor de la clave Aragorn.
def merge(dict1, dict2):
    merged_dict = {}
    for key in dict1:
        merged_dict[key] = dict1[key]
    for key in dict2:
        merged_dict[key] = dict2[key]
    return merged_dict

    
            

print(merge({"Frodo": 56, "Aragorn": 10}, {"Aragorn": 100, "Gandalf": 809}))
print(merge({"Frodo": 56, "Aragorn": 10}, {"Gandalf": 809}))
print(merge({"Gandalf": 56}, {"Aragorn": 100, "Gandalf": 809}))
print(merge({"Frodo": 56, "Aragorn": 10}, {}))
