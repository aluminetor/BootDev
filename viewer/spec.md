# Especificación — Visor de apuntes BootDev ("Learning Dashboard / Cheatsheet")

> Versión 1.0 · Estado: **aprobada** · Fecha: 2026-10-10

## 1. Objetivo

Visor web local, estático y de solo lectura que muestra los ficheros del curso BootDev como una cheatsheet navegable: teoría (comentarios y docstrings) intercalada con el código resuelto, organizada por curso → capítulo → ejercicio.

## 2. Decisiones acordadas

| # | Tema | Decisión |
|---|------|----------|
| 1 | Indexación | JSON local (`viewer/data/index.json`) generado por `viewer/build_index.py` (solo stdlib). Se vuelve a ejecutar a mano cuando hay ficheros nuevos. |
| 2 | Información por ejercicio | Código resuelto con resaltado de sintaxis, teoría extraída (`#` y `"""`) y metadatos del fichero (capítulo, nº de ejercicios, fecha de modificación). |
| 3 | Navegación | Barra lateral con árbol de 3 niveles: Curso → Capítulo → Ejercicio. Al hacer clic en un ejercicio se va a su posición dentro de la vista del capítulo. |
| 4 | Alcance | `CHxx_*.py` = capítulos; el resto de `.py` del curso = "Extras"; `README.md` = portada. Se ignoran `.agents/`, `skills-lock.json`, `viewer/`, `.git/`. |

## 3. Hallazgos del análisis de los ficheros

Los ficheros actuales **no siguen un separador uniforme**:

| Fichero | Líneas | Separadores `#****#` | Otros marcadores |
|---|---|---|---|
| `CH01_firstbug.py` | 24 | 0 | Comentarios cortos tipo título (`#¿Qué es el código?`) |
| `CH02_variables.py` | 151 | 1 | Comentarios de título (`# Cadenas F en Python`) |
| `CH03_functions.py` | 339 | 0 | Cabecera `## FUNCTIONS ##`, títulos (`# Multiple Parameters`) |
| `Desafios.py` | 82 | 0 | — |

Por eso la segmentación (sección 5.3) se basa en varias reglas, aplicadas por orden de prioridad, y no solo en `#****#`.

## 4. Glosario

- **Curso**: carpeta de primer nivel con ficheros de estudio (p. ej. `PythonBeginners/`).
- **Capítulo**: fichero que cumple `^CH(\d{2})_(\w+)\.py$`.
- **Extra**: cualquier otro `.py` dentro de un curso (p. ej. `Desafios.py`).
- **Ejercicio**: bloque de un capítulo delimitado según las reglas de 5.3.
- **Segmento**: trozo continuo de un ejercicio, de tipo `theory` (comentarios/docstrings) o `code`.
- **Comentarios de plantilla**: líneas de BootDev como `# don't touch below this line`.

## 5. Requisitos funcionales (EARS)

### 5.1 Generación del índice (`build_index.py`)

- **RF-01** — CUANDO el usuario ejecute `python viewer/build_index.py`, EL SISTEMA recorrerá las carpetas de curso de la raíz del repositorio y escribirá `viewer/data/index.json` en UTF-8.
- **RF-02** — EL SISTEMA tratará como curso toda carpeta de primer nivel que contenga al menos un `.py`, excepto `viewer/`, `.agents/`, `.git/` y las carpetas ocultas.
- **RF-03** — CUANDO un fichero cumpla el patrón `CHxx_*.py`, EL SISTEMA lo registrará como capítulo con `number = xx` y un título legible derivado del nombre (`CH03_functions` → "Functions").
- **RF-04** — CUANDO un `.py` de un curso no cumpla el patrón de capítulo, EL SISTEMA lo registrará en la sección `extras` de ese curso.
- **RF-05** — CUANDO exista `README.md` en la raíz, EL SISTEMA incluirá su contenido en bruto como `home.markdown` del índice.
- **RF-06** — EL SISTEMA abrirá los ficheros de estudio solo para lectura y nunca los modificará, formateará, renombrará ni moverá.
- **RF-07** — EL SISTEMA guardará por fichero: ruta relativa, número de líneas, fecha de última modificación (ISO 8601) y número de ejercicios.
- **RF-08** — EL SISTEMA ordenará los capítulos por número y los extras por nombre.
- **RF-09** — SI un fichero no se puede decodificar como UTF-8, ENTONCES EL SISTEMA volverá a intentarlo con `utf-8-sig` y `cp1252`, y si sigue fallando, lo registrará con `error` y continuará con los demás.
- **RF-10** — CUANDO termine, EL SISTEMA mostrará en consola un resumen en español (cursos, capítulos, extras, ejercicios y avisos).
- **RF-11** — EL SISTEMA usará solo la biblioteca estándar de Python (`pathlib`, `json`, `re`, `tokenize`/`ast`, `datetime`).

### 5.2 Extracción de teoría y código

- **RF-12** — EL SISTEMA clasificará como `theory` las líneas de comentario `#` y los literales de cadena triple (`"""` / `'''`) que estén solos como sentencia (docstrings o bloques de notas).
- **RF-13** — EL SISTEMA clasificará como `code` el resto de líneas que no estén en blanco y conservará la indentación original.
- **RF-14** — CUANDO haya líneas consecutivas del mismo tipo, EL SISTEMA las unirá en un solo segmento y guardará el número de línea donde empieza y donde acaba.
- **RF-15** — EL SISTEMA quitará el prefijo `#` (y un espacio opcional) y las comillas triples de los segmentos `theory`, sin tocar el resto del texto.
- **RF-16** — SI un comentario está al final de una línea de código (`x = 1  # nota`), ENTONCES EL SISTEMA lo dejará dentro del segmento `code`.
- **RF-17** — CUANDO un comentario coincida con una frase de plantilla (`don't touch below/above this line`), EL SISTEMA lo dejará en el segmento `code` y lo marcará como `boilerplate`, en lugar de tratarlo como teoría.
- **RF-18** — SI la tokenización falla (código con errores de sintaxis a propósito), ENTONCES EL SISTEMA usará un análisis línea a línea con expresiones regulares y añadirá un aviso.

### 5.3 Segmentación en ejercicios

- **RF-19** — CUANDO una línea cumpla `^#\*{3,}#?\s*$`, EL SISTEMA cerrará el ejercicio actual y empezará uno nuevo (regla de prioridad 1).
- **RF-20** — CUANDO una línea cumpla `^##\s*(.+?)\s*##\s*$`, EL SISTEMA empezará un ejercicio nuevo con ese texto como título (regla de prioridad 2).
- **RF-21** — CUANDO un segmento `theory` de una sola línea (≤ 60 caracteres, sin punto final) vaya después de un segmento `code` y antes de una línea en blanco, EL SISTEMA lo tomará como título y empezará un ejercicio nuevo (regla de prioridad 3, p. ej. `# Multiple Parameters`).
- **RF-22** — SI un ejercicio no tiene título, ENTONCES EL SISTEMA le pondrá "Ejercicio N", donde N es su posición dentro del capítulo.
- **RF-23** — SI un fichero no tiene ningún delimitador, ENTONCES EL SISTEMA lo tratará como un único ejercicio.
- **RF-24** — EL SISTEMA descartará los ejercicios que solo tengan líneas en blanco o separadores.

### 5.4 Carga del visor

- **RF-25** — CUANDO se abra `viewer/index.html`, EL SISTEMA cargará `data/index.json` con `fetch` y pintará la barra lateral y la portada.
- **RF-26** — SI no se puede cargar `index.json` (404 o JSON no válido), ENTONCES EL SISTEMA mostrará un mensaje en español con el comando `python viewer/build_index.py` para generarlo.
- **RF-27** — SI la página se abre con `file://`, ENTONCES EL SISTEMA avisará de que hay que servirla con `python -m http.server 8000`.
- **RF-28** — EL SISTEMA funcionará sin conexión, sin CDN ni dependencias externas.

### 5.5 Navegación (barra lateral)

- **RF-29** — EL SISTEMA mostrará un árbol plegable de 3 niveles: Curso → Capítulos (y un grupo "Extras") → Ejercicios.
- **RF-30** — CUANDO el usuario haga clic en un capítulo o extra, EL SISTEMA mostrará la vista de ese fichero en el panel principal y desplegará sus ejercicios en el árbol.
- **RF-31** — CUANDO el usuario haga clic en un ejercicio, EL SISTEMA abrirá la vista de su capítulo (si no estaba abierta) y se desplazará hasta ese ejercicio.
- **RF-32** — EL SISTEMA guardará la selección actual en la URL (`#/PythonBeginners/CH03_functions/3`) para que se pueda recargar y compartir.
- **RF-33** — CUANDO la página cargue con un hash válido, EL SISTEMA abrirá directamente ese capítulo y ejercicio.
- **RF-34** — SI el hash apunta a un capítulo o ejercicio que no existe, ENTONCES EL SISTEMA mostrará la portada y un aviso que no bloquee la página.
- **RF-35** — MIENTRAS el usuario se desplace por un capítulo, EL SISTEMA resaltará en el árbol el ejercicio visible.
- **RF-36** — CUANDO el usuario haga clic en el título de la aplicación, EL SISTEMA mostrará la portada con el `README.md` renderizado.
- **RF-37** — MIENTRAS la ventana mida menos de 768 px, EL SISTEMA ocultará la barra lateral detrás de un botón de menú.
- **RF-38** — EL SISTEMA permitirá recorrer el árbol con el teclado (Tab, Enter y flechas) y usará roles ARIA de árbol.

### 5.6 Vista de capítulo

- **RF-39** — CUANDO se muestre un capítulo, EL SISTEMA mostrará una cabecera con número, título, ruta, nº de ejercicios, nº de líneas y fecha de modificación en formato local español.
- **RF-40** — EL SISTEMA mostrará cada ejercicio como una sección con su título y sus segmentos en el orden original.
- **RF-41** — EL SISTEMA mostrará los segmentos `theory` como texto legible, sin aspecto de código, y conservará los saltos de párrafo.
- **RF-42** — EL SISTEMA mostrará los segmentos `code` en un bloque monoespaciado, con números de línea del fichero original y resaltado de sintaxis Python (palabras clave, cadenas, números, comentarios, built-ins).
- **RF-43** — EL SISTEMA hará el resaltado con un tokenizador propio en `app.js`, sin librerías externas.
- **RF-44** — EL SISTEMA mostrará las líneas `boilerplate` con menos contraste visual.
- **RF-45** — EL SISTEMA escapará todo el contenido de los ficheros antes de insertarlo en el DOM (sin `innerHTML` con texto sin escapar).
- **RF-46** — SI un fichero tiene `error` en el índice, ENTONCES EL SISTEMA mostrará el aviso en lugar del contenido.

## 6. Requisitos no funcionales

- **RNF-01** — HTML5, CSS con variables (`--color-*`, `--space-*`) y JS en ES modules sin variables globales y sin paso de build.
- **RNF-02** — Código en inglés; interfaz, mensajes y documentación en español.
- **RNF-03** — Ningún cambio fuera de `viewer/` (se comprueba con `git status`).
- **RNF-04** — Consola de DevTools sin errores ni 404 con el índice actual.
- **RNF-05** — Pintar un capítulo de 500 líneas en menos de 100 ms en un equipo de escritorio normal.
- **RNF-06** — Contraste de texto AA (WCAG 2.1) en teoría y código.

## 7. Formato propuesto de `index.json`

```json
{
  "schemaVersion": 1,
  "generatedAt": "2026-10-10T16:00:00-05:00",
  "home": { "path": "README.md", "markdown": "# BootDev ..." },
  "courses": [
    {
      "id": "PythonBeginners",
      "title": "Python Beginners",
      "path": "PythonBeginners",
      "chapters": [
        {
          "id": "CH03_functions",
          "kind": "chapter",
          "number": 3,
          "title": "Functions",
          "path": "PythonBeginners/CH03_functions.py",
          "lineCount": 339,
          "modifiedAt": "2026-10-08T21:14:03-05:00",
          "exerciseCount": 6,
          "warnings": [],
          "exercises": [
            {
              "index": 1,
              "title": "FUNCTIONS",
              "startLine": 1,
              "endLine": 88,
              "segments": [
                { "type": "theory", "startLine": 2, "endLine": 4,
                  "text": "Pero queremos reutilizar nuestro código! ..." },
                { "type": "code", "startLine": 6, "endLine": 17,
                  "text": "def area_of_circle(r):\n    pi = 3.14\n ...",
                  "boilerplateLines": [] }
              ]
            }
          ]
        }
      ],
      "extras": [
        { "id": "Desafios", "kind": "extra", "title": "Desafios",
          "path": "PythonBeginners/Desafios.py", "...": "misma forma que un capítulo, sin number" }
      ]
    }
  ]
}
```

## 8. Estructura de ficheros

```
viewer/
├── index.html
├── styles.css
├── app.js
├── build_index.py
└── data/
    └── index.json   (generado)
```

## 9. Fuera de alcance (v1)

Búsqueda de texto, etiquetas de conceptos clave, botón de copiar, ejecutar código, editar ficheros, indexar `.md`/`.html`/`.css`/`.js` de futuros cursos y regenerar el índice automáticamente.

## 10. Criterios de aceptación

1. `python viewer/build_index.py` termina sin errores y genera el índice con 1 curso, 3 capítulos y 1 extra.
2. Con `python -m http.server 8000`, `http://localhost:8000/viewer/` muestra la portada con el README.
3. Cada capítulo muestra la teoría y el código en el mismo orden y con las mismas líneas que el fichero original.
4. Navegar por el hash y recargar la página mantiene la vista.
5. DevTools sin errores y `git status` sin cambios fuera de `viewer/`.

## 11. Decisiones cerradas

1. **Regla de títulos (RF-21)**: aprobada. Los comentarios cortos que parecen títulos abren un ejercicio nuevo.
2. **Markdown de la portada**: aprobado un parser mínimo propio en `app.js` que soporta títulos, párrafos, listas, bloques de código, código en línea, negrita/cursiva y enlaces.

- **RF-47** — CUANDO se muestre la portada, EL SISTEMA convertirá `home.markdown` a HTML con el parser mínimo, escapando antes todo el texto.
