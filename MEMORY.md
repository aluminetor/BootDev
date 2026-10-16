# Memoria del proyecto — Visor local de apuntes BootDev

Memoria breve para continuar el proyecto entre sesiones. El visor presenta los
apuntes de Boot.dev y no modifica los archivos originales de estudio.

## Estado actual

- Visor funcional en `viewer/`: `index.html`, `styles.css`, `app.js` y `data/index.json`.
- Catálogo indexado: 1 curso, 9 capítulos + 1 archivo de retos, 62 ejercicios y 42 conceptos de glosario.
- Capítulos recientes: `CH09_lists.py` completado e indexado (8 ejercicios).
- Web estática sin framework ni build step (HTML, CSS moderno, JS ES modules).
- Skill local `.agents/skills/sync-viewer/` creada para automatizar la sincronización.
- `viewer/build_index.py` genera el índice a partir de `README.md` y las carpetas de estudio.

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
