# ==============================================================================
# MÓDULO 9: COMPUTACIÓN, MATEMÁTICAS Y OPERACIONES BIT A BIT
# ==============================================================================

# ------------------------------------------------------------------------------
# 9.1 Números, Operadores Matemáticos y Notación Científica
# ------------------------------------------------------------------------------
# - Enteros (int): números sin decimales (positivos o negativos).
# - División de piso (//): divide y redondea hacia abajo al entero más cercano.
# - Exponentes (**): eleva un número a una potencia (ej. 3**2 = 9).
# - Incremento in situ (+=): suma y reasigna en un solo paso.
# - Guiones bajos (_): mejoran la lectura visual de números grandes sin afectar su valor.

def calculate_damage(sword, arrow, spear, dagger, fireball):
    total_damage = sword + arrow + spear + dagger + fireball
    average_damage = total_damage / 5
    return total_damage, average_damage

print("Daño total y promedio:", calculate_damage(3, 5, 2, 1, 4))
print("División entera (11 // 2):", 11 // 2)
print("División entera negativa (-7 // 3):", -7 // 3)
print("Potencia (3**2):", 3 ** 2)

star_rating = 4
star_rating += 1
print("Rating actualizado:", star_rating)

# Notación científica: `e` mueve el punto decimal a la derecha (+) o izquierda (-)
print("16e3:", 16e3)       # 16000.0
print("7.1e-2:", 7.1e-2)   # 0.071


# Ejercicio: Capacidad máxima de servidores
def max_players_on_server():
    small_server = 1.024e18
    medium_server = 1.024e19
    large_server = 1.024e20
    return small_server, medium_server, large_server

print("Servidores:", max_players_on_server())


# Ejercicio: Delimitadores de miles para legibilidad
def calculate_dps(damage, time):
    dps = damage / time
    print(f"Damage per second: {dps:.2f}")

calculate_dps(8_000_000, 45)
calculate_dps(10_000_000, 49)
print("=====================================")


# ------------------------------------------------------------------------------
# 9.2 Operadores Lógicos (Booleanos)
# ------------------------------------------------------------------------------
# - `and`: True solo si AMBOS lados son True.
# - `or`: True si AL MENOS UNO es True.
# - `not`: invierte el valor booleano.

print("True and True:", True and True)
print("True or False:", True or False)
print("(True or False) and False:", (True or False) and False)
print("not True:", not True)
print("=====================================")


# ------------------------------------------------------------------------------
# 9.3 Sistema Binario (Base 2) y Conversiones
# ------------------------------------------------------------------------------
# Cada posición de derecha a izquierda vale el doble: 1, 2, 4, 8, 16, 32...
# En Python, el prefijo `0b` indica un número escrito en binario.

# Tu función manual de decimal a binario:
def decimal_binario(num):
    if num < 1:
        return 0
    cociente = num
    binario = ""
    while cociente >= 1:
        cociente, residuo = cociente // 2, cociente % 2
        binario = str(residuo) + binario
    return int(binario)

print("13 en binario (manual):", decimal_binario(13))


# Conversión nativa de cadena binaria a entero usando `int(cadena, base)`
def binary_string_to_int(num_servers, num_players, num_admins):
    return int(num_servers, 2), int(num_players, 2), int(num_admins, 2)

print("Binarios a enteros:", binary_string_to_int("100", "101", "10010"))
print("=====================================")


# ------------------------------------------------------------------------------
# 9.4 Operadores Bit a Bit (Bitwise `&` y `|`) y Máscaras de Permisos
# ------------------------------------------------------------------------------
# Operan columna por columna sobre los bits de dos números (ver tabla superior):
# - `&` (AND): devuelve 1 solo si ambos bits son 1 (ideal para VERIFICAR permisos).
# - `|` (OR): devuelve 1 si al menos uno de los bits es 1 (ideal para COMBINAR permisos).

print("0b0101 & 0b0111 =", bin(0b0101 & 0b0111))  # 0b101 (5)
print("0b0101 | 0b0111 =", bin(0b0101 | 0b0111))  # 0b111 (7)

# Ejercicio: Permisos del gremio mediante Bitmask
can_create_guild = 0b1000
can_review_guild = 0b0100
can_delete_guild = 0b0010
can_edit_guild   = 0b0001

def get_create_bits(user_permissions):
    return user_permissions & can_create_guild

def get_review_bits(user_permissions):
    return user_permissions & can_review_guild

def get_delete_bits(user_permissions):
    return user_permissions & can_delete_guild

def get_edit_bits(user_permissions):
    return user_permissions & can_edit_guild

usuario = 0b0101  # Permisos activos: Revisar (0100) y Editar (0001)
print("¿Puede revisar gremio?:", bool(get_review_bits(usuario)))
print("¿Puede crear gremio?:", bool(get_create_bits(usuario)))
