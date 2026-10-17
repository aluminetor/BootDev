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

