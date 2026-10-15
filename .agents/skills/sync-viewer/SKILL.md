---
name: sync-viewer
description: Sincroniza y verifica los cambios de ejercicios BootDev en el visor web local sin tocar archivos de estudio.
---

# Sync Viewer — Guía de Sincronización y Verificación

Esta skill automatiza y estandariza el flujo de sincronización del visor web local (`viewer/`) cada vez que se añaden o modifican ejercicios, capítulos o apuntes de BootDev (ej. en `PythonBeginners/`). Garantiza la consistencia de datos sin vulnerar los límites del proyecto.

---

## 1. Guardarraíl de Lectura Estricta (Límites Inviolables)

Antes de ejecutar cualquier acción, el agente debe interiorizar y respetar estrictamente las siguientes restricciones:

- **Archivos de estudio de solo lectura:** NUNCA modificar, formatear, mover ni renombrar archivos dentro de las carpetas de estudio (ej. `PythonBeginners/`, `PythonBeginners/Desafios.py`, o futuras carpetas de cursos). El visor únicamente los consume en modo lectura.
- **Cero dependencias externas:** NO instalar ni sugerir instalar paquetes de `npm`, librerías de `pip` o frameworks. Toda la solución opera exclusivamente con HTML5/CSS/JavaScript nativo (ES Modules) y la biblioteca estándar (`stdlib`) de Python.
- **Aislamiento del visor:** Todos los cambios del sistema visor deben residir exclusivamente dentro del directorio `viewer/` o en archivos de documentación operativa (`MEMORY.md`).

---

## 2. Secuencia de Ejecución de Sincronización

Sigue rigurosamente esta secuencia de 5 pasos en orden:

### Paso 1: Regenerar el índice

Ejecuta el script generador desde la raíz del repositorio:

```powershell
python viewer/build_index.py
```

El script analizará `README.md` y todos los archivos de estudio (`CHxx_*.py`, `Desafios.py`), reconstruyendo `viewer/data/index.json`.

---

### Paso 2: Inspección de integridad de datos

Verifica que el índice generado cumpla con los estándares de integridad:

1. **Codificación y formato:**
   - Asegurar que `viewer/data/index.json` exista, esté codificado en UTF-8 y sea un JSON sintácticamente válido.
2. **Métricas del catálogo:**
   - Extraer y reportar al usuario las métricas clave resultantes de la ejecución:
     - Número total de cursos.
     - Número total de capítulos indexados.
     - Número total de ejercicios detectados.
     - Número de conceptos del glosario procesados.
   - Detallar los ejercicios contabilizados por cada archivo/capítulo.

> [!NOTE]
> Si el script arroja 0 ejercicios para un archivo en progreso o recién creado, reportarlo para que el usuario conozca su estado en el árbol de navegación.

---

### Paso 3: Verificación de estado Git

Inspecciona el estado del repositorio mediante:

```powershell
git status
```

**Criterios de validación:**
- Comprobar que los únicos cambios modificados o no rastreados correspondan intencionadamente a:
  - Los archivos de estudio trabajados por el usuario (ej. `PythonBeginners/CHxx_*.py`).
  - El índice actualizado `viewer/data/index.json`.
  - La memoria `MEMORY.md` y/o skills creadas en `.agents/skills/`.
- ⚠️ **Alerta inmediata:** Si se detectan modificaciones accidentales en archivos de estudio que no debían tocarse o en archivos del visor no relacionados con la tarea, detener el flujo y notificar de inmediato al usuario antes de continuar.

---

### Paso 4: Actualización de Memoria (`MEMORY.md`)

De acuerdo con las reglas del repositorio, actualiza `MEMORY.md`:

1. **Reflejar el estado actualizado:**
   - Número de ejercicios y conceptos actualmente indexados.
   - Capítulos o ejercicios recién incorporados o modificados.
2. **Brevedad obligatoria:**
   - Mantener el archivo conciso (máximo ~50 líneas).
   - Eliminar o resumir información histórica que haya quedado obsoleta.
3. **Privacidad:**
   - No registrar credenciales, tokens ni datos sensibles.

---

### Paso 5: Instrucciones de verificación local en el navegador

Instruye al usuario (o ejecuta si procede) los pasos de validación visual:

1. **Iniciar servidor local:**
   Debido a las políticas CORS y la carga dinámica de módulos ES y `index.json`, no se debe abrir el archivo con `file://`. Usar el servidor HTTP integrado de Python desde la raíz:
   ```powershell
   python -m http.server 8000
   ```
2. **Navegación:**
   Abrir en el navegador:
   [http://localhost:8000/viewer/](http://localhost:8000/viewer/)
3. **Validación en DevTools (F12):**
   - **Consola:** Comprobar que no existan excepciones JavaScript (`Uncaught SyntaxError`, `TypeError`, etc.).
   - **Red (Network):** Asegurar que no haya solicitudes con estado 404 ni fallos al obtener `viewer/data/index.json` o recursos CSS/JS.
   - **Interfaz:** Comprobar que el árbol de navegación lateral muestre los nuevos capítulos, que la vista de teoría/código renderice correctamente los bloques y que el filtro de búsqueda/glosario responda adecuadamente.
