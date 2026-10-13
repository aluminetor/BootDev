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