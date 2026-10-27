# Memoria del proyecto — Visor local de apuntes BootDev

Memoria breve para continuar el proyecto entre sesiones. El visor presenta los
apuntes de Boot.dev y no modifica los archivos originales de estudio.

## Estado actual

- Visor funcional en `viewer/`: `index.html`, `styles.css`, `app.js` y `data/index.json`.
- Catálogo indexado: 1 curso, 14 capítulos + 1 archivo de retos, 102 ejercicios y 42 conceptos de glosario.
- Capítulos recientes: `CH13_type_hints.py` (10 ejercicios) y `CH14_practice.py` (15 ejercicios) completados e indexados (102 ejercicios totales).
- Se creó `CH13_type_hints_organized.py` en la raíz como copia organizada del capítulo; el original en `PythonBeginners/` permanece intacto.
- Web estática sin framework ni build step (HTML, CSS moderno, JS ES modules).
- Skill local `.agents/skills/sync-viewer/` creada para automatizar la sincronización.
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

- Usar la skill `sync-viewer` tras añadir o modificar ejercicios de estudio.
- Verificar en `http://localhost:8000/viewer/` y validar en consola de DevTools (sin 404 ni errores JS).
