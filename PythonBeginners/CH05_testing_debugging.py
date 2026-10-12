# ## Pruebas unitarias

# Un nuevo tipo de lección
# A partir de ahora, te encontrarás con un nuevo tipo de lección: las pruebas unitarias . Una prueba unitaria es simplemente un programa automatizado que prueba una pequeña "unidad" de código. Normalmente, solo una o dos funciones.

# 1 El main.py archivo que contiene tu código
# 2 El main_test.pya rchivo que contiene las pruebas unitarias

### Dos tipos de lecciones
# Como ya comentamos, en Boot.dev hay dos tipos de lecciones de programación:

# lecciones sobre la salida de la consola
# Lecciones de prueba de unidad
# Lecciones sobre la salida de la consola
# Solo un archivo de código, generalmente con un comentario que explica dónde escribir el código.
# Cuando "envías" tu código, la salida de la consola debe coincidir exactamente con la salida esperada para que se apruebe.
# Las instrucciones de depuración printharán que su código no se envíe correctamente, así que elimínelas antes de enviarlo.
# Lecciones de prueba de unidad
# 2 archivos de código: mainy main_test. Puedes leer las pruebas, pero no puedes editarlas.
# Cuando "envías" tu código, los valores de retorno de tus funciones deben coincidir exactamente con los valores esperados para que se apruebe.
# La salida de la consola se ignora, puedes dejar printinstrucciones de depuración en tu código.

### Depuración

# Cuando trabajas como desarrollador profesional, normalmente escribes el código en tu ordenador y lo pruebas tú mismo antes de implementarlo para los usuarios.

# Aprender de forma eficaz
# Este curso está a punto de volverse un poco más difícil . No hay vuelta de hoja: si programar fuera pan comido, todos ganarían sueldos de seis cifras como ingenieros de software. Pero no lo es, y para tener éxito sin estancarse ni frustrarse, hay que aprender a aprender.

# Proceso para resolver problemas de codificación rígida
# ¡Lee la lección primero! Analiza los ejemplos antes de escribir tu propio código.
# Lee la tarea. Comprende el objetivo de la tarea antes de empezar a escribir código.
# Empieza a escribir código.
# Agrega instrucciones print(). No esperes a escribir mucho código para empezar a probarlo. Agrega print()instrucciones y usa el Runbotón para ver si tu código hace lo que esperas en cada paso. Es más fácil encontrar problemas en pequeños fragmentos de código que en grandes bloques.
# Sigue ejecutando, imprimiendo y corrigiendo hasta que estés seguro de que tu código funciona correctamente.
# Envía tu código . Si la tarea incluye pruebas unitarias, no es necesario eliminar las print()instrucciones de depuración. Si la tarea consiste en probar la salida de la consola, asegúrate de eliminarlas print()antes de enviarla.
# Compara tu código con el del instructor. No se te penalizará por consultar la solución una vez que hayas completado la tarea con éxito.
# Información adicional
# Intenta usar Boots antes de consultar la solución. Boots es bastante útil para darte pistas precisas que te ayudarán a resolver el problema por tu cuenta.
# No hay problema en consultar la solución de vez en cuando cuando te quedas completamente atascado, pero no lo conviertas en un hábito . Si notas que siempre te quedas atascado, deberías reiniciar el capítulo o el curso para asegurarte de comprender el material.
# Puedes restablecer el código de una tarea con el ↶botón "restablecer". Por ejemplo, quizás olvidaste qué modificaciones hiciste y qué código dejó el instructor.
# Puedes restablecer todo el código almacenado en caché desde la página de configuración. Esto es útil si quieres reiniciar un curso o capítulo.
# Rastreo de pila
# Un rastreo de pila (o "traceback") es un mensaje de error de aspecto alarmante que el intérprete de Python imprime en la consola cuando encuentra ciertos problemas. Los rastreos de pila son más comunes (al menos para ti ahora mismo) cuando intentas ejecutar código Python no válido.

# Como programador, debes acostumbrarte a descifrar mensajes de error intimidantes. Mejor empezamos ahora.

# Asignación
# Ejecuta el código en su estado actual. Deberías ver algo como esto:

# File "main.py", line 3
#     msg = f"You have {strength} strength, {wisdom} wisdom, and {dexterity} dexterity for a total of {total} stats.
#                                                                                                                   ^
# SyntaxError: unindent does not match any outer indentation level

# File "main.py", line 3

# Este es el inicio del rastreo. El propósito de un rastreo es guiarnos paso a paso por la ruta que siguió el intérprete de Python a través de nuestro código antes de encontrar un error. ¡En la mayoría de los casos, esto nos ayudará a descubrir qué salió mal!

# En este caso, el intérprete estaba ejecutando el código del main.pyarchivo cuando encontró un error en la línea 3.

# msg = f"You have {strength} strength, {wisdom} wisdom, and {dexterity} dexterity for a total of {total} stats.

# Esta es la línea de código exacta que provocó el error.

# SyntaxError: unindent does not match any outer indentation level

# Este es el tipo de error. En este caso, se SyntaxErrortrata de un error general relacionado con código inválido. El intérprete de Python esperaba cierta cantidad de sangría (espacio en blanco al principio de la línea), pero no encontró lo que se esperaba.
