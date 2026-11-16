# Memoria del proyecto — Visor local de apuntes BootDev

Memoria breve para continuar el proyecto entre sesiones. El visor presenta los
apuntes de Boot.dev y no modifica los archivos originales de estudio.

## Estado actual

- Visor funcional en `viewer/`: `index.html`, `styles.css`, `app.js`, `build_index.py`, `test_build_index.py` y `data/index.json`.
- Catálogo indexado: 1 curso, 14 capítulos + 1 archivo de retos, 102 ejercicios y 42 conceptos de glosario.
- Pruebas unitarias en `viewer/test_build_index.py` (stdlib `unittest`, 9 pruebas pasando).
- Navegación mejorada: paginación Anterior/Siguiente entre capítulos, botón "Volver arriba", teclado en árbol/búsqueda y botón para copiar enlace de cada ejercicio.
- Web estática sin framework ni build step (HTML, CSS moderno, JS ES modules).
- Skill local `.agents/skills/sync-viewer/` para automatizar la sincronización.
- `viewer/build_index.py` genera el índice a partir de `README.md` y las carpetas de estudio.
- README actualizado con el certificado de Introduction to Python enlazado a Boot.dev.
- README actualizado para reflejar la estructura actual de `PythonBeginners/`, `viewer/` y los archivos de configuración.

## Decisiones importantes

- Archivos de estudio (`PythonBeginners/` y otros) son estrictamente de solo lectura.
- Sin dependencias externas: solo stdlib de Python y JavaScript nativo.
- El navegador consume `viewer/data/index.json` servido localmente.
- Teoría extraída de docstrings/comentarios; código resuelto como bloques separados.
- Glosario y conceptos se indexan automáticamente con expresiones regulares.

## Errores a evitar

- No añadir npm, pip ni dependencias externas sin autorización previa.
- Tras modificar o agregar capítulos, regenerar índice con `python viewer/build_index.py`.
- No abrir con `file://`; levantar servidor local con `python -m http.server 8000`.
- Mantener UTF-8 y verificar con `git status` que no haya cambios fuera de lo previsto.

## Próximos pasos

- Ejecutar `python -m unittest discover -s viewer -v` tras cambiar `viewer/build_index.py`.
- Usar la skill `sync-viewer` tras añadir o modificar ejercicios de estudio.
- Verificar en `http://localhost:8000/viewer/` y validar en consola de DevTools (sin 404 ni errores JS).
