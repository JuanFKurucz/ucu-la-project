# Mi asistente — LLMs en Acción

El punto de partida de tu proyecto: un asistente que responde preguntas sobre un tema que elegís, con tus
documentos. Lo escribís vos, en seis versiones. Acá solo están las carpetas, las librerías (con `uv`) y un
chequeo del entorno.

## Empezar

1. Arriba, **Use this template → Create a new repository**: dueño vos, visibilidad **Private**.
2. En tu repo nuevo: *Settings → Collaborators* → invitá a **JuanFKurucz**.
3. Clonalo con GitHub Desktop y abrí la carpeta en VS Code. En la terminal, parado en la carpeta:

```bash
uv sync
uv run python check_setup.py --fixture
```

4. Copiá `.env.example` como `.env` y pegá **solo** tu clave adentro. Después:

```bash
uv run python check_setup.py
```

Tiene que terminar en `OK: entorno listo.`

## Las carpetas

```
mi-asistente/
├── config.toml        qué modelo usar, temperatura y tope de salida
├── llm.py             cargar_modelo(): el modelo de config.toml, con errores en castellano
├── check_setup.py     ¿funciona tu entorno?
├── corpus/            tus documentos (.md o .txt)
├── datos/             tus entradas y tus preguntas de prueba (.jsonl)
├── evidencia/         una página por versión: qué cambiaste, con qué resultado y por qué
├── docs/              arquitectura y registro de evaluación (entrega final)
├── tests/             tus pruebas: uv run pytest
└── logs/              lo que dejan tus corridas (no se sube)
```

## Lo que escribís en cada versión

Cada versión es un archivo nuevo con una función `responder`. Lo que entra y lo que sale está fijo, así
podés comparar una versión con otra con las mismas preguntas.

| Versión | Archivo | Entra | Sale |
|---|---|---|---|
| `v0.1` | `v01_api.py` | `pregunta: str` | `dict` con `respuesta`, `tokens_entrada`, `tokens_salida`, `latencia_s`; cada llamada, una línea en `logs/v01.jsonl` |
| `v0.2` | `v02_rag.py` | `pregunta: str` | lo de `v0.1` más `fuentes`: los fragmentos de `corpus/` que usó |
| `v0.3` | `v03_memoria.py` | `pregunta: str`, `hilo: str` | lo de `v0.2`; recuerda lo dicho en el mismo `hilo` |
| `v0.4` | `v04_agente.py` | `pregunta: str` | lo de `v0.2` más `herramientas`: cuáles usó (documentos, web, calculadora) |
| `v0.5` | `v05_equipo.py` | `pregunta: str` | lo de `v0.4` más `aprobada: bool`: una persona aprueba antes de responder |
| `v1.0` | `v10_produccion.py` | `pregunta: str` | lo de `v0.5` más `costo_usd` y una traza por pregunta en `logs/` |

Antes de `v0.1`, en la clase 2, escribís también `m2_extraccion.py` (práctica M2). Las prácticas de cada módulo
dicen cómo construir cada versión, paso a paso: https://juanfkurucz.com/ucu-la/

## Las entregas

En cada fecha el docente mira tu repo **tal como está ese día** y te devuelve comentarios. Qué se espera en cada
una, con ejemplos: la consigna del proyecto y la tarea de cada entrega, en el aula virtual.

| Entrega | Hasta | Versión | Lo que tiene que funcionar |
|---|---|---|---|
| 1 | mar 3/11, 23:59 | `v0.1` | Le preguntás al modelo sobre tu tema y responde; queda guardado qué, cuánto tardó y cuántos tokens usó |
| 2 | mar 10/11, 23:59 | `v0.2` | Responde con tus documentos y dice de cuál sacó cada dato; si no está, lo dice |
| 3 | mar 17/11, 23:59 | `v0.3`, `v0.4` | Recuerda la conversación y elige entre tus documentos, internet y una calculadora |
| Final | dom 22/11, 23:59 | `v0.5`, `v1.0` | Un equipo de agentes con una persona que aprueba; sabés cuánto cuesta y otra persona lo corre con tu README |

## Reglas

- La clave vive en `.env`. Nunca en el código, en un chat ni en una captura.
- Datos personales no van al modelo. Tus documentos son públicos o autorizados.
- Cada versión se sube con *commit* y *push*, con su página en `evidencia/` (`v0.1.md`, `v0.2.md`…). El
  mensaje del *commit* empieza con la versión («v0.2: …»).
- Antes de correr, **predecí**. Después, **compará** con las mismas preguntas.
