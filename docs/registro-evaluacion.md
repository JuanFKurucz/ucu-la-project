# Registro de evaluación — [nombre del sistema]

Guardalo en tu repo como `docs/registro-evaluacion.md` (en Markdown); al aula virtual va el enlace del repo. Qué pide
la entrega final: la [consigna](https://github.com/JuanFKurucz/ucu-la-project/blob/main/CONSIGNA.md).

## Suite

Cuántas preguntas tenés por `tipo`, escrito como en tus suites (M4: `documental`, `sintesis`, `sin_respuesta`,
`adversarial`; M6: `corpus`, `web`, `calculo`, `ninguna`, `combinada` y, del «Para casa», `ambigua`), y el enlace a tus
archivos de preguntas (`datos/…jsonl`).

Para la entrega: 20 preguntas propias (de tus documentos, de síntesis, sin respuesta, con web, de cálculo y 2 que
intenten engañar al sistema), cada una con su respuesta esperada, su herramienta y su documento de origen.
Ojo con las sin respuesta (`"fuentes": []`): tu v0.2 y tu v0.3 responden «NO ENCONTRADO» porque su `SISTEMA` lo pide; el
del agente (v0.4 en adelante) no. Sumale esa regla, o juzgá esas preguntas a mano y no reportes la abstención.

## Resultados por versión

Todo sale de `medir.py`, con las mismas preguntas antes y después.

| Comparación | Métrica | Antes | Después | Lo que no cambió |
|---|---|---:|---:|---|
| *Ejemplo: fragmento de 1000 → 400* | *hit* | *10/11* | *11/11* | *mismas 13 preguntas, mismo modelo* |
| Sin documentos / con documentos | correctas (tu juicio) | | | preguntas y modelo |
| Búsqueda inicial / con una perilla cambiada | hit | | | preguntas y modelo; una sola perilla |
| v0.2 / v0.3 (con LangChain) | hit · correctas | | | preguntas, modelo y perillas |
| Agente: elegir la herramienta | eligió bien (x/n, la columna `eligio_bien`) | | | preguntas de selección y modo de web |
| Agente solo / equipo | correctas · llamadas por pregunta (más llamadas = más costo) · latencia mediana | | | preguntas y modo de web |

«Correctas» la decidís vos: en la tabla de `medir.py`, o en `logs/medir.csv` abierto en Excel o Power BI, marcá cuáles
están bien y escribilo como `8/13`. Si una fila dio un error del proveedor (cuota, red, modelo mal escrito), repetí la
medición: esa fila no mide tu sistema.

**Consistencia (pass^3):** la medición final va 3 veces, con las mismas preguntas. Guardá cada tabla con otro nombre
(`logs/medir-1.csv`, `-2` y `-3`: cambiá el nombre en el `to_csv` de `medir.py`), marcá en cada una cuáles están bien y
contá cuántas salen bien **en las 3**: en Excel o Power BI, una columna por medición y una que diga si las tres son «sí».
Reportá eso y no solo el promedio: un LLM acierta una vez y erra la siguiente. Antes de correr tres veces, mirá la
columna `llamadas`: el equipo hace varias por pregunta, y la cuota gratis es por día. Anotá con qué `web` mediste (la
real, o la grabada si lo declarás).

## Ejemplos (mínimo 5)

Salen de tu tabla de `medir.py` (o de `logs/medir.csv`): la pregunta, la respuesta, las `fuentes` o las `herramientas`, y
lo que esperabas (si no coinciden, es un fallo de búsqueda o de elección). Elegí aciertos y fallos (los fallos van también
abajo). Copiá los textos en la tabla: `logs/` no se sube al repositorio, así que quien lea tu registro no los ve.

| Pregunta | Respuesta del sistema | Fuente o herramienta | ¿Correcta? | Análisis |
|---|---|---|---|---|
| *¿Qué recargo tiene una cuota pagada el día 25?* | *«2 %, venció el día 10 [reglamento]»* | *buscar_documentos → reglamento* | *Sí* | *El fragmento correcto llegó primero.* |

## Fallos representativos

Al menos 2, cada uno con su causa probable:

- **búsqueda**: el fragmento con la respuesta no llegó (M4);
- **redacción**: llegó y el modelo lo ignoró o lo leyó mal (M4);
- **elección de herramienta**: pidió otra herramienta o ninguna (M6);
- **coordinación**: en el equipo, el supervisor repartió mal o una nota no llegó al redactor (M7).

Si hiciste el análisis de errores de la clase 7 (la tabla dinámica de tus fallas), usá esas etiquetas.

## Costo y operación

El costo por pregunta y por mes (M8: `medir.py` con el costo), con los precios reales de tu modelo y su fecha
(`PRECIO_FECHA`), sacados de la página del proveedor. Tu práctica de producción y su evidencia: un extracto de la traza
(sin claves ni datos personales), tu test, la caché medida o la evaluación continua.
