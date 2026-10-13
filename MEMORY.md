# Memoria del proyecto — Visor local de apuntes BootDev

Memoria breve para continuar el proyecto entre sesiones. El visor presenta los
apuntes de Boot.dev y no modifica los archivos originales de estudio.

## Estado actual

- Visor funcional en `viewer/`: `index.html`, `styles.css`, `app.js` y `data/index.json`.
- Aplicación web estática sin framework ni build step; usa HTML, CSS moderno y JavaScript ES modules.
- `PythonBeginners/` contiene los capítulos CH01–CH07 y `Desafios.py`.
- El índice actual reúne 41 ejercicios y se acompaña de un glosario de 42 conceptos.
- El visor ofrece árbol de navegación, vista de capítulo, búsqueda, filtro por conceptos,
  resaltado de sintaxis, tema claro/oscuro y navegación mediante hash.
- `viewer/build_index.py` genera el índice a partir de `README.md` y de las carpetas de estudio.

## Decisiones importantes

- Los archivos de `PythonBeginners/` son de solo lectura: no editarlos, formatearlos,
  moverlos ni renombrarlos desde el visor.
- No se usan dependencias externas. El generador utiliza únicamente la biblioteca
  estándar de Python y el navegador ejecuta JavaScript nativo.
- El navegador consume `viewer/data/index.json` porque no puede leer directamente el disco.
- La teoría se extrae de docstrings y comentarios; el código resuelto se conserva como
  segmentos separados.
- Los títulos de ejercicios solo se reconocen cuando tienen al menos dos palabras para
  evitar falsos positivos en comentarios cortos.
- El glosario y los conceptos relacionados se calculan durante la generación del índice
  mediante expresiones regulares sobre la teoría y el código.

## Errores a evitar

- No añadir npm, pip, frameworks ni servicios externos sin pedir autorización.
- Tras cambiar capítulos, glosario o el parser, regenerar el índice con:
  `python viewer/build_index.py`.
- No abrir el visor con `file://`; usar un servidor local para que funcionen los módulos
  y la carga de JSON:
  `python -m http.server 8000`.
- Mantener las lecturas en UTF-8 y conservar el formato generado de `index.json`.
- Comprobar que `git status` solo muestre cambios intencionados, especialmente dentro de
  `viewer/`; no corregir problemas ajenos a la tarea.

## Próximos pasos

- Añadir nuevos capítulos únicamente en las carpetas de estudio correspondientes y
  regenerar el índice.
- Verificar en `http://localhost:8000/viewer/` el árbol, la búsqueda, los conceptos y
  cada capítulo después de cambios relevantes.
- Revisar la consola del navegador para detectar errores de JavaScript o recursos 404.
