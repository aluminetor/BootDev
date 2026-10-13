# AGENTS.md — Visor local de apuntes BootDev

## 1. Stack y estructura
- Web estática sin framework: HTML5 + CSS moderno + JavaScript (ES modules), sin build step.
- El navegador no puede leer el disco, así que un script `viewer/build_index.py` (solo stdlib de Python) recorre las carpetas de estudio y genera `viewer/data/index.json`.
- Estructura nueva, toda dentro de `viewer/`: `index.html`, `styles.css`, `app.js`, `build_index.py`, `data/`.
- Carpetas de estudio (solo lectura): `PythonBeginners/`, `README.md`, `skills-lock.json`, `.agents/`.
- Secciones del visor: árbol de carpetas → capítulo (`CHxx_*.py`) → teoría (docstrings y comentarios) + código resuelto.

## 2. Convenciones
- Código en inglés: variables, funciones, clases, nombres de archivo y commits.
- Interfaz y notas en español: textos visibles, etiquetas, mensajes y documentación.
- Nombres claros y descriptivos (`renderChapterList`, no `rcl`). Funciones pequeñas con una sola responsabilidad.
- CSS con variables (`--color-*`, `--space-*`); JS sin variables globales, con `const`/`let`.

## 3. Forma de trabajar
- Por fases: (1) analizar la estructura → (2) proponer un plan → (3) implementar → (4) verificar.
- Antes de escribir código, valida la estructura de carpetas y el formato de `index.json` con el usuario.
- Haz cambios pequeños y revisables; resume qué se ha tocado al terminar cada fase.

## Memoria
- Al empezar, lee `MEMORY.md` para conocer el estado del proyecto y las decisiones
tomadas.
- Al terminar una tarea, actualízalo: estado actual, decisiones importantes (con su
porqué) y errores a evitar.
- Mantenlo breve (máximo ~50 líneas): resume o elimina lo que ya no aporte.
- Si algo se convierte en una regla permanente, propón moverlo a `AGENTS.md` en lugar de
dejarlo en la memoria.
- No guardes nunca datos sensibles (claves, tokens, datos personales). 


## 4. Límites
- ✅ Siempre: respetar los archivos originales de estudio (`.py`, `.md`, `.json`); el visor solo los lee.
- ⚠️ Preguntar antes: añadir dependencias (npm, frameworks, librerías pip), reestructurar o renombrar carpetas.
- 🚫 Prohibido: modificar, formatear o mover los ejercicios resueltos de BootDev (`PythonBeginners/` y futuras carpetas de cursos).
- ✅ Siempre: actualizar `MEMORY.md` al terminar cada tarea

## 5. Verificación
1. Regenerar el índice: `python viewer/build_index.py`
2. Servir en local: `python -m http.server 8000` (desde la raíz del repo)
3. Abrir `http://localhost:8000/viewer/` y comprobar el árbol, la teoría y el código de cada capítulo.
4. Revisar la consola de DevTools (F12): sin errores ni 404.
5. Confirmar con `git status` que no hay cambios fuera de `viewer/`.
