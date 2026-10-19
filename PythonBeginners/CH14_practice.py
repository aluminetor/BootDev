# Suma de números
# En este capítulo vamos a afianzar los conceptos que hemos aprendido mediante la resolución de una serie de problemas prácticos.

# Asignación
# Completa la number_sumfunción. Debe sumar todos los números desde 1hasta ny devolver el resultado. Si nes menor que 1, devuelve 0. Por ejemplo:

# number_sum(5) -> 1+2+3+4+5 -> 15
# number_sum(3) -> 1+2+3 -> 6
# Recuerda que la rangeletra a no incluirá el último número.

def number_sum(n: int) -> int:
    number_sum = 0
    for number in range(1, n + 1):
        number_sum +=number

    return number_sum
        
#=====================================================#
       
# Encuentra Min
# En este problema necesitarás una forma de representar el número más grande posible: infinito . En Python, puedes usar esta constante para representar el infinito positivo:

my_infinity: float = float("inf")

# Asignación
# Escribe una funciónfind_min() que encuentre el número más pequeño en una lista. Si la lista está vacía, devuelve float("inf"). Por ejemplo:

# find_min([1, 3, -1, 2]) -> -1
# find_min([18, 3, 7, 2]) -> 2
# Intenta hacerlo sin funciones integradas como min()o sorted().

def find_min(nums: list[int]) -> int | float:
    min: float = float("inf")
    for num in nums:
        if num < min:
            min = num
    return min
print(find_min([1, 3, -1, 2]))  # Output: -1

#=====================================================#

# Eliminar números no enteros
# type()La función integrada se puede utilizar para obtener el tipo de una variable. Por ejemplo:

# type(1) is int
# # True

# type("1") is str
# # True

# type(1.0) == float
# # True

# type("seventy-six") == int
# # False

# Asignación
# Completa la remove_nonints()función. Recibe una lista y devuelve una nueva lista, pero sin los tipos que no sean enteros.

# new_list: list[int] = remove_nonints(["1", 1, "3", "400", 4, 500])
# print(new_list)
# # [1, 4, 500]

# No modifique la numslista de entrada. Devuelva una nueva lista con solo los números enteros.

def remove_nonints(nums: list[object]) -> list[int]:
    new_nums: list[int] = []
    for num in nums:
        if type(num) is int:
            new_nums.append(num)
    return new_nums

print(remove_nonints(["1", 1, "3", "400", 4, 500]))  # Output: [1, 4, 500]
#=====================================================#
# Factorial
# Un factorial es el producto (resultado de la multiplicación) de todos los enteros positivos menores o iguales a un número dado. Por ejemplo:

# 1! = 1 = 1
# 2! = 2 * 1 = 2
# 3! = 3 * 2 * 1 = 6
# 4! = 4 * 3 * 2 * 1 = 24
# 5! = 5 * 4 * 3 * 2 * 1 = 120
# También existe un caso especial para el cero:

# 0! = 1
# Es simplemente 1 una definición de los expertos en matemáticas (los que viven en la torre de marfil).

# Asignación
# Completa la factorial()función. Debe devolver el factorial de un número dado.

# En matemáticas, el !símbolo representa un factorial, pero no es un operador factorial válido en Python. Utilice un bucle y la multiplicación para calcular el resultado correcto.
def factorial(num: int) -> int:
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result
print(factorial(5))  # Output: 120

#=====================================================#

# Suma de área
# El área de un rectángulo se calcula multiplicando su altura por su anchura. Por ejemplo, el área de un rectángulo con una altura de 3y una anchura de 5es:

# 3 * 5 = 15



# Asignación
# Completa la area_sum()función. Acepta una lista de rectángulos, donde cada rectángulo es un diccionario que tiene la siguiente estructura:

# rectangle: dict[str, int] = {"height": 5, "width": 6}

# La función debe calcular el área de cada rectángulo y devolver la suma de todas las áreas .

def area_sum(rectangles: list[dict[str, int]]) -> int:
    sum = 0
    for rectangle in rectangles:
        sum += rectangle["height"] * rectangle["width"]
    return sum

print(area_sum([{"height": 5, "width": 6}, {"height": 3, "width": 4}]))  # Output: 42
#=====================================================#

# División de listas
# Recuerda que en Python puedes dividir dos números usando el /operador. Por ejemplo:

print(6 / 2)  # 3.0
print(8 / 4)  # 2.0

# También puedes iterar sobre cada elemento de una lista usando un for inbucle. Por ejemplo:

numbers: list[int] = [1, 7, 3, 2, 5]
for num in numbers:
    print(num)
# 1
# 7
# 3
# 2
# 5

# Asignación
# Completa la divide_list()función. Recibe como entrada una lista y un número, y debe devolver una nueva lista que contenga todos los elementos de la lista original después de dividirlos por el segundo valor de entrada .

# Por ejemplo:

# divided_list: list[float] = divide_list([6, 8, 10], 2)
# print(divided_list)
# # [3.0, 4.0, 5.0]

# No redondee los números decimales resultantes; simplemente devuélvalos tal cual.

def divide_list(nums: list[int], divisor: int) -> list[float]:
    new_list: list[float] = []
    for num in nums:
        new_list.append(num / divisor)
    return new_list

print(divide_list([6, 8, 10], 2))  # Output: [3.0, 4.0, 5.0]
#=====================================================#

# Unir cuerdas
# El +operador en Python se puede usar para concatenar (combinar) cadenas. Por ejemplo:

print("hello" + " " + "world")
# hello world

author: str = "Tolkien"
message: str = "The " + "world never deserved " + author
print(message)
# The world never deserved Tolkien

# Asignación
# Completa la join_strings()función. Recibe una lista de cadenas y devuelve una nueva cadena individual.

# La nueva cadena es la concatenación de todas las cadenas de entrada de la lista, una tras otra, en orden, separadas por una coma . Si la lista está vacía, devuelve una cadena vacía. Por ejemplo:
"""
string_list: list[str] = ["Annie", "Reiner", "Bertholdt"]
joined_string: str = join_strings(string_list)
print(joined_string)
# "Annie,Reiner,Bertholdt"

string_list = ["Eren", "Mikasa", "Armin"]
joined_string = join_strings(string_list)
print(joined_string)
# "Eren,Mikasa,Armin"
"""
# No utilice el método integrado .join()... estamos intentando aprender cómo funciona esto manualmente .


def join_strings(strings: list[str]) -> str:
    joined = ""
    for s in strings:
        joined += s + ","
    return joined[:-1] #La sintaxis concat[:-1] es una operación de rebanado ( slicing ) en Python, y lo que hace es crear una copia de la cadena excluyendo el último caracter .

print(join_strings(["Annie", "Reiner", "Bertholdt"]))
# La sintaxis general del rebanado es secuencia[inicio:fin]:

# inicio: Si se deja vacío (antes de los dos puntos :), Python asume que empieza desde el índice 0.
# fin: Indica hasta dónde llegar (sin incluir ese índice). En Python, los índices negativos cuentan desde el final hacia atrás. Por lo tanto, -1hace referencia al último elemento.
# Al escribir [:-1], te estás diciendo Python:

# "Toma todos los caracteres desde el principio ( 0) hasta el último elemento ( -1), sin incluirlo."
#=====================================================#


# Pruebas unitarias
# Si terminas trabajando como programador, pasarás mucho tiempo escribiendo tus propias pruebas unitarias . Hasta ahora te hemos proporcionado pruebas unitarias , pero es útil saber cómo funcionan.

# Cuando realizas tus propias pruebas, normalmente utilizas una biblioteca para escribir y ejecutar pruebas. Por ejemplo, en Python, pytest y unittest son bastante populares.

# Pero también está bien escribir pruebas desde cero en ocasiones. En Boot.dev lo hacemos para que las pruebas se integren correctamente con nuestro entorno en línea. Ese es el propósito del main_test.pyarchivo: un conjunto de pruebas personalizado que hemos escrito para cada una de tus lecciones.

# Asignación
# Vamos a cambiar el enfoque: en main.pyencontrarás una función de solo lectura , casiavg_luck_boost correcta, llamada . Se utiliza en Fantasy Quest para calcular el aumento promedio de "suerte" otorgado a un grupo de jugadores cuando derrotan a un jefe, para determinar el botín que reciben.

# La función se puede utilizar de la siguiente manera:

luck_boosts: list[int] = [5, 3, 10]
avg_boost: float = avg_luck_boost(luck_boosts)
print(avg_boost)  # 6.0

# Ejecuta las pruebas. ¡ Observa que todas pasan! Pero hay un problema... algunos comportamientos extraños no están cubiertos por los casos de prueba existentes.

# ¿Qué sucede si ningún miembro del grupo tiene bonificación de suerte? La función intentará dividir por cero, es decir, por la longitud de la lista de entrada, y el programa fallará.

# luck_boosts: list[int] = []
# avg_boost: float = avg_luck_boost(luck_boosts)  # ZeroDivisionError

# Lo que queremos que haga esta función si la lista de entrada está vacía es devolver 0.0. Añade ese resultado esperado a test_cases.py; corregiremos la función en la próxima lección.

# Agregue un nuevo diccionario a la run_caseslista, con luck_boostsestablecido a una lista vacía y expected_avgestablecido a 0.0.
"""
def avg_luck_boost(luck_boosts: list[int]) -> float:
    total = 0
    for boost in luck_boosts:
        total += boost
    return total / len(luck_boosts)



run_cases: list[dict[str, list[int] | float]] = [
    {
        "luck_boosts": [5, 3, 10],
        "expected_avg": 6.0,
    },
    {
        "luck_boosts": [7],
        "expected_avg": 7.0,
    },
    {
        "luck_boosts": [4, 4, 4],
        "expected_avg": 4.0,
    },
    {
        "luck_boosts": [2, 3],
        "expected_avg": 2.5,
    },
    {
        "luck_boosts": [],
        "expected_avg": 0.0,
    },
]

"""

# Solucionar una prueba fallida
# ¡Tenemos un caso de prueba fallido para nuestra avg_luck_boostfunción! Cuando se le pasa una lista vacía a la función, debería devolver 0.0. En cambio, intenta dividir por cero y falla.

# Vamos a actualizar avg_luck_boostpara que todas las pruebas vuelvan a pasar.

# A algunos programadores les gusta trabajar de esta manera; se llama " desarrollo guiado por pruebas " (TDD):

# Crea una función básica.
# Escribe pruebas que esperen el comportamiento correcto de esa función.
# Ejecuta las pruebas (deberían fallar).
# Implementa la función y ve actualizándola hasta que pase las pruebas.
# El desarrollo guiado por pruebas (TDD) a veces es un tema controvertido, y no profundizaremos en ello aquí. Sin embargo, en cursos posteriores les brindaremos mucha más práctica con la escritura de pruebas.

# Asignación
# Corrige la avg_luck_boostfunción en main.py.

# Al inicio de la función, compruebe si luck_boostsla lista está vacía. Si es así, simplemente retorna 0.0para evitar un error de división por cero.


def avg_luck_boost(luck_boosts: list[int]) -> float:
    if len(luck_boosts) == 0:
        return 0.0
    total = 0
    for boost in luck_boosts:
        total += boost
    return total / len(luck_boosts)
print(avg_luck_boost([5, 3, 10]))  # Output: 6.0
print(avg_luck_boost([]))  # Output: 0.0

