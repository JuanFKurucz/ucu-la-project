# LLMs en Acción · Proyecto: qué se espera en cada entrega

Octubre – Noviembre 2026 · Facultad de Ingeniería y Tecnologías · Maestría en Ciencia de Datos

## El proyecto

Construís, solo, un **asistente que responde sobre un tema que elegís**, con tus documentos (al menos 5). Crece en 6 versiones y cada una funciona sola. Cada entrega tiene algo que tiene que **funcionar** y una página donde contás **qué probaste y qué decidiste**.

| Entrega | Fecha | Qué tiene que funcionar |
|---|---|---|
| 1 | mar 3/11, 23:59 | Tu primer programa con un LLM |
| 2 | mar 10/11, 23:59 | Tu asistente busca en tus documentos |
| 3 | mar 17/11, 23:59 | Recuerda la conversación y elige herramientas |
| Final | dom 22/11, 23:59 | Tu asistente terminado |

### Cómo arrancar

1. Desde la plantilla https://github.com/JuanFKurucz/ucu-la-project: **Use this template**, repo **privado**.
2. Invitá a **JuanFKurucz** como colaborador (*Settings → Collaborators*).
3. Clonalo con GitHub Desktop y seguí «Antes de la clase 1» del aula virtual.
4. Pegá el enlace en la tarea «Enlace a tu repositorio».

Cada versión la escribís vos con la práctica del módulo (https://juanfkurucz.com/ucu-la/), que te da el código paso a paso.

### Cómo se entrega

En cada fecha el docente mira tu repo **tal como está ese día** y te devuelve comentarios. Antes, revisá:

- Corre con `uv run python …`, parado en la carpeta del proyecto.
- `.env` **no** aparece en los cambios de GitHub Desktop.
- Hiciste *commit* (el mensaje empieza con la versión: «v0.1: …») y *push*.
- Está la página de evidencia, en `evidencia/` (`v0.1.md`, `v0.2.md`…), con tus números.
- Pegaste el enlace al repo en la tarea del aula virtual.

### Cómo se corrige cada entrega de avance

10 puntos, 2 por cada cosa:

- **Corre** de punta a punta.
- **Explicás** qué hace tu código y por qué lo armaste así.
- **Comparás** antes y después con las mismas preguntas.
- **Decidís** con esos números y nombrás algo que todavía falla.
- **Declarás** cómo usaste IA.

## Entrega de avance 1 · Tu primer programa con un LLM

**Tu primer programa con un LLM.** Versión `v0.1` · hasta el mar 3/11, 23:59 (antes de la clase 3) · 10 puntos · sale de: prácticas M2 y M3 (clase 2).

**Lo que tiene que funcionar.** Una llamada a un LLM andando: le preguntás sobre tu tema, responde, y queda guardado qué respondió, cuánto tardó y cuántos tokens usó. Si algo falla, no se cae.

**En BI sería:** una consulta programada que deja su registro de ejecución: qué pidió, qué devolvió, cuánto tardó y cuánto costó (los tokens son lo que se cobra).

| Si hacés esto | Tenés que ver |
|---|---|
| Corrés `uv run python v01_api.py` con «¿Qué es una alucinación en un LLM?» | La respuesta aparece de a poco, en dos frases, con sus tokens y su tiempo |
| Lo corrés con tus 5 preguntas | `logs/v01.jsonl` tiene 5 renglones nuevos, uno por pregunta |
| Ponés en `config.toml` un modelo que no existe | Avisa el error en castellano, reintenta, lo anota y sigue |
| Corrés `uv run python m2_extraccion.py` | Saca entidad y cifra de 10 textos y dice cuántos acertó |

**Qué subís.** `v01_api.py`, `m2_extraccion.py`, `tabla.py`, tus 5 textos en `datos/` y `evidencia/v0.1.md`.

**En tu página de evidencia contás:**

- ¿Qué cambiaste en el molde de M2 y cuántos aciertos hubo antes y después?
- ¿Qué configuración elegís para tu v0.1 (modelo o mensaje del sistema) y por qué?
- ¿Qué pasó con el modelo que no existe? ¿Sirvió reintentar?
- ¿Cuánto costaría por mes, a 1000 preguntas por día? (con el precio y su fecha)
- Cómo usaste IA: qué aceptaste, corregiste o rechazaste.

## Entrega de avance 2 · Tu asistente busca en tus documentos

**Tu asistente busca en tus documentos.** Versión `v0.2` · hasta el mar 10/11, 23:59 (antes de la clase 5) · 10 puntos · sale de: práctica M4 (clases 3 y 4).

**Lo que tiene que funcionar.** Tu asistente responde con tus documentos y dice de cuál sacó cada dato. Si la respuesta no está en ellos, lo dice en vez de inventar.

**En BI sería:** un reporte con la fuente al pie de cada número; si el dato no está en tus tablas, lo dice en vez de rellenar.

| Si hacés esto | Tenés que ver |
|---|---|
| Preguntás algo que está en tus documentos | Responde con tus documentos y nombra el archivo de cada dato |
| Preguntás algo que no está en tus documentos | Dice que no lo encuentra, sin inventar |
| Corrés tus preguntas de prueba sin y con documentos | Ves cuántas respondió bien en cada caso |

**Qué subís.** Al menos 5 documentos de tu tema en `corpus/`, tus preguntas de prueba en `datos/`, `v02_rag.py`, `medir.py` y `evidencia/v0.2.md`.

**En tu página de evidencia contás:**

- Con las mismas preguntas, ¿cuántas bien sin documentos y cuántas con documentos?
- Un error: ¿no encontró el fragmento, o lo encontró y respondió mal?
- ¿Qué tamaño de fragmento (los pedazos en que partís tus documentos para buscar) elegiste y por qué?
- ¿Qué hiciste con los comentarios de la entrega 1?
- Cómo usaste IA: qué aceptaste, corregiste o rechazaste.

## Entrega de avance 3 · Recuerda la conversación y elige herramientas

**Recuerda la conversación y elige herramientas.** Versión `v0.3` y `v0.4` · hasta el mar 17/11, 23:59 (antes de la clase 7) · 10 puntos · sale de: prácticas M5 y M6 (clases 4 a 6).

**Lo que tiene que funcionar.** Tu asistente recuerda lo que hablaste en la misma conversación y elige solo entre tus documentos, internet y una calculadora. Si una herramienta falla, lo dice.

**En BI sería:** un filtro que se mantiene durante la sesión (la memoria) y un asistente que decide qué fuente consultar: tus documentos, internet o la calculadora.

| Si hacés esto | Tenés que ver |
|---|---|
| Decís «Mi tema es la cooperativa Las Acacias» y después preguntás «¿De qué es mi tema?» | Responde «la cooperativa Las Acacias»; en otra conversación, no lo sabe |
| Preguntás «¿Cuánto es el 18 % de 3.400.000?» | Usa la calculadora: 612.000 |
| Preguntás algo de actualidad que no está en tus documentos | Busca en internet y dice de dónde lo sacó |
| Internet no responde | Lo dice, en vez de inventar |

**Qué subís.** `v03_memoria.py`, `v04_agente.py`, `medir.py`, tus preguntas con la herramienta esperada en `datos/`, `evidencia/v0.3.md` y `evidencia/v0.4.md`.

**En tu página de evidencia contás:**

- Con las mismas preguntas, ¿v0.3 responde igual o mejor que v0.2?
- ¿Cómo comprobaste que dos conversaciones no se mezclan?
- ¿Cuántas veces eligió bien la herramienta, antes y después de tu cambio?
- ¿Qué hiciste con los comentarios de la entrega 2?
- Cómo usaste IA: qué aceptaste, corregiste o rechazaste.

## Entrega final · Tu asistente terminado

**Tu asistente terminado.** Versión `v0.5` y `v1.0` · hasta el dom 22/11, 23:59 (antes de la clase 8, lun 23/11) · 60 puntos, con la rúbrica del programa · sale de: prácticas M7 y M8 (clases 6 y 7).

**Lo que tiene que funcionar.** Un equipo de agentes (un supervisor reparte: uno investiga, otro calcula, otro redacta) responde sobre tu tema, y una persona aprueba antes de cada respuesta. Sabés cuánto cuesta y otra persona lo puede correr con tu README.

**En BI sería:** un flujo con aprobación antes de publicar y con el registro de cada corrida (la traza) y su costo; el README son las instrucciones para que otra persona lo instale.

| Si hacés esto | Tenés que ver |
|---|---|
| Hacés una pregunta que necesita tus documentos y una cuenta | El equipo la resuelve y te pide que apruebes |
| Rechazás la respuesta | No se envía |
| Mirás la traza de una pregunta | Qué herramientas usó, cuántos tokens y cuánto costó |
| Otra persona clona tu repo y sigue tu README | El asistente corre |

**Qué subís.** Tu repo con `v1.0`, `tests/test_produccion.py` y su README, `docs/arquitectura.md`, `docs/registro-evaluacion.md` y, en la tarea, el PDF de tus slides.

**En tu página de evidencia contás:**

- ¿El equipo es mejor que el agente solo de v0.4? (aciertos, llamadas y tiempo, con las mismas preguntas)
- ¿Cuánto cuesta por mes y qué protección pusiste, con su prueba?
- ¿Lo liberarías? ¿Qué falta?
- Cómo usaste IA: qué aceptaste, corregiste o rechazaste.

### Cómo se corrige la entrega final

| Criterio | Peso |
|---|---:|
| Funciona: cumple los 4 requisitos y la demo anda | 30 |
| Decisiones: podés defender por qué elegiste cada parte | 25 |
| Búsqueda en tus documentos: encuentra lo relevante y lo mediste | 20 |
| Herramientas: el agente elige bien, de forma consistente | 15 |
| Producción: una práctica (traza, caché, protección o costo) que aporta | 10 |

Más complejidad no suma sola: vale más una comparación honesta que un sistema grande sin evidencia.

## Defensa y nota

En la última clase, 35 minutos a solas con el docente, sin IA: presentás (20 min), respondés preguntas sobre todo tu sistema (8) y recorrés tu código (7). Se puntúa sobre 30 y da un factor: **1** (24 a 30), **0,8** (15 a 23), **0,5** (0 a 14) o **0** si el proyecto no es tuyo.

**Nota = factor de la defensa × (proyecto final + entregas de avance) + controles de lectura.**

Proyecto final 60 · entregas de avance 30 · controles de lectura 10. Ejemplo: 54 + 27 = 81; con defensa de 20 (factor 0,8), 64,8; más 8 de controles, **72,8**.
