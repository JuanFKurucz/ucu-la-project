# LLMs en Acción · Proyecto: qué se espera en cada entrega

Octubre – Noviembre 2026 · Facultad de Ingeniería y Tecnologías · Maestría en Ciencia de Datos

## El proyecto

Construís, solo, un **asistente que responde sobre un tema que elegís**, con tus documentos (al menos 5). Crece en 6 versiones y cada una funciona sola. Cada entrega tiene algo que tiene que **funcionar** y una página donde contás **qué probaste y qué decidiste**.

| Entrega | Fecha | Qué tiene que funcionar |
|---|---|---|
| 1 | mié 4/11, 23:59 | Tu primer programa con un LLM |
| 2 | mié 11/11, 23:59 | Tu asistente busca en tus documentos |
| 3 | mié 18/11, 23:59 | Recuerda la conversación y elige herramientas |
| Final | dom 22/11, 23:59 | Tu asistente terminado |

### Cómo arrancar

1. Desde la plantilla https://github.com/JuanFKurucz/ucu-la-project: **Use this template**, repo **privado**.
2. Invitá a **JuanFKurucz** como colaborador (*Settings → Collaborators*).
3. Clonalo con GitHub Desktop y seguí «Antes de la clase 1» del aula virtual.
4. Pegá el enlace en la tarea «Enlace a tu repositorio».

Esta consigna dice **qué** tiene que hacer tu asistente. **Cómo** hacerlo lo practicás en clase: cada versión sale de las prácticas de su módulo (https://juanfkurucz.com/ucu-la/), y lo adaptás a tu tema con tus decisiones.

### Cómo se entrega

En cada fecha el docente mira tu repo **tal como está ese día** y te devuelve comentarios. Antes, revisá:

- Tu asistente anda: lo probás de cero con los casos de la entrega.
- Tu clave **no** está en el repo.
- Subiste tus cambios a GitHub (*commit* y *push*).
- Está tu página de evidencia de la versión, con tus números.
- Pegaste el enlace al repo en la tarea del aula virtual.

### Cómo se corrige cada entrega de avance

10 puntos, 2 por cada cosa:

- **Corre** de punta a punta.
- **Explicás** qué hace tu código y por qué lo armaste así.
- **Comparás** antes y después con las mismas preguntas.
- **Decidís** con esos números y nombrás algo que todavía falla.
- **Declarás** cómo usaste IA.

## Entrega de avance 1 · Tu primer programa con un LLM

**Tu primer programa con un LLM.** Versión `v0.1` · hasta el mié 4/11, 23:59 (el día de la clase 3) · 10 puntos · sale de: prácticas M2 y M3 (clase 2).

**Lo que tiene que funcionar.** Un solo pedido al modelo: unas instrucciones sobre tu tema (si querés, con algunos datos pegados) y la pregunta. Responde, y queda anotado qué respondió, cuánto tardó y cuántos tokens usó (lo que se cobra). Si el servicio del modelo falla, avisa y no se cae. Todavía no busca en documentos ni usa herramientas: eso viene en las entregas que siguen.

**En BI sería:** una consulta programada que deja su registro de ejecución: qué pidió, qué devolvió, cuánto tardó y cuánto costó (los tokens son lo que se cobra).

*Ejemplos con una cooperativa: en tu tema cambian las palabras, no lo que tiene que pasar.*

| Cuando | Tiene que pasar |
|---|---|
| Pegaste en las instrucciones los datos básicos de la cooperativa (horario, fecha de la asamblea) y un socio pregunta «¿Cuándo es la próxima asamblea?» | Responde con lo que le diste, en dos frases que van apareciendo mientras las escribe, y vos ves cuánto tardó y cuánto costó |
| A fin de mes querés saber qué le preguntaron y cuánto gastó | Tenés el registro de cada consulta: qué le preguntaron, qué respondió, cuánto tardó y cuánto costó |
| El servicio del modelo falla (se cayó, o se terminó la cuota del día) | Te avisa en castellano qué pasó, lo intenta de nuevo y sigue con la próxima pregunta |
| Le pasás una noticia: «La cooperativa Las Acacias informó que cerró 2025 con 1.250 socios activos» | Te devuelve el dato listo para una tabla: organización «Cooperativa Las Acacias», cifra 1250 |
| Le pasás 10 noticias que ya revisaste a mano | Sabés en cuántas sacó bien el dato |

**Qué subís.** Tu asistente andando, tus textos y preguntas de prueba, y tu página de evidencia de la v0.1.

**En tu página de evidencia contás:**

- ¿Qué cambiaste en el pedido para que extraiga bien, y cuántos aciertos hubo antes y después?
- ¿Qué configuración elegís (modelo o instrucciones) y por qué?
- Cuando simulaste la falla del servicio, ¿qué hizo tu asistente? ¿Sirvió intentarlo de nuevo?
- ¿Cuánto costaría por mes, a 1000 preguntas por día? (con el precio y su fecha)
- Cómo usaste IA: qué aceptaste, corregiste o rechazaste.

## Entrega de avance 2 · Tu asistente busca en tus documentos

**Tu asistente busca en tus documentos.** Versión `v0.2` · hasta el mié 11/11, 23:59 (el día de la clase 5) · 10 puntos · sale de: práctica M4 (clases 3 y 4).

**Lo que tiene que funcionar.** Tu asistente responde con tus documentos y dice de cuál sacó cada dato. Si la respuesta no está en ellos, lo dice en vez de inventar.

**En BI sería:** un reporte con la fuente al pie de cada número; si el dato no está en tus tablas, lo dice en vez de rellenar.

*Ejemplos con una cooperativa: en tu tema cambian las palabras, no lo que tiene que pasar.*

| Cuando | Tiene que pasar |
|---|---|
| Un socio pregunta «¿Cuántos días tengo para presentar un reclamo?», y la respuesta está en el reglamento | Responde con el plazo del reglamento y dice de qué documento lo sacó, como la fuente al pie de un reporte |
| Pregunta algo que tus documentos no dicen | Responde que no lo encuentra, en vez de inventar algo creíble |
| Comparás: las mismas preguntas, sin tus documentos y con ellos | Sabés cuántas respondió bien en cada caso |

**Qué subís.** Tu asistente andando, al menos 5 documentos de tu tema, tus preguntas de prueba y tu página de evidencia de la v0.2.

**En tu página de evidencia contás:**

- Con las mismas preguntas, ¿cuántas bien sin documentos y cuántas con documentos?
- Un error: ¿no encontró lo que buscaba (falla de recuperación), o lo encontró y respondió mal (de generación)?
- ¿En qué tamaño partiste tus documentos (el tamaño de fragmento, `chunk_size`) y cuántos fragmentos traés (`k`), y por qué?
- ¿Qué hiciste con los comentarios de la entrega 1?
- Cómo usaste IA: qué aceptaste, corregiste o rechazaste.

## Entrega de avance 3 · Recuerda la conversación y elige herramientas

**Recuerda la conversación y elige herramientas.** Versión `v0.3` y `v0.4` · hasta el mié 18/11, 23:59 (el día de la clase 7) · 10 puntos · sale de: prácticas M5 y M6 (clases 4 a 6).

**Lo que tiene que funcionar.** Tu asistente recuerda lo que hablaste en la misma conversación y elige solo entre tus documentos, internet y una calculadora. Si una herramienta falla, lo dice.

**En BI sería:** un filtro que se mantiene durante la sesión (la memoria) y un asistente que decide qué fuente consultar: tus documentos, internet o la calculadora.

*Ejemplos con una cooperativa: en tu tema cambian las palabras, no lo que tiene que pasar.*

| Cuando | Tiene que pasar |
|---|---|
| Un socio pregunta «¿Cuándo vence la cuota?» y después «¿Y si pago tarde?» | Entiende que la segunda es sobre la cuota; en otra conversación, con otro socio, empieza de cero |
| Le preguntás «El presupuesto es de 3.400.000 y sube 18 %: ¿cuánto queda?» | Hace la cuenta con la calculadora, no de memoria: 4.012.000 |
| Le preguntás algo reciente que no está en tus documentos (una noticia de esta semana) | Busca en internet y dice de dónde lo sacó |
| La búsqueda en internet se cae | Te dice que no pudo buscar, en vez de inventar la respuesta |

**Qué subís.** Tu asistente andando, tus preguntas de prueba con la herramienta que esperás en cada una, y tus páginas de evidencia de la v0.3 y la v0.4.

**En tu página de evidencia contás:**

- Con las mismas preguntas, ¿v0.3 responde igual o mejor que v0.2?
- ¿Cómo comprobaste que dos conversaciones no se mezclan?
- ¿Cuántas veces eligió bien la herramienta, antes y después de tu cambio?
- ¿Qué hiciste con los comentarios de la entrega 2?
- Cómo usaste IA: qué aceptaste, corregiste o rechazaste.

## Entrega final · Tu asistente terminado

**Tu asistente terminado.** Versión `v0.5` y `v1.0` · hasta el dom 22/11, 23:59 (antes de la clase 8, lun 23/11) · 60 puntos, con la rúbrica del programa · sale de: prácticas M7 y M8 (clases 6 y 7).

**Lo que tiene que funcionar.** Un equipo de agentes (un supervisor reparte: uno investiga, otro calcula, otro redacta) responde sobre tu tema, y una persona aprueba antes de cada respuesta. Sabés cuánto cuesta, un dato personal no se escapa y otra persona lo puede instalar con tu README.

**En BI sería:** un flujo con aprobación antes de publicar y con el registro de cada corrida (la traza) y su costo; el README son las instrucciones para que otra persona lo instale.

*Ejemplos con una cooperativa: en tu tema cambian las palabras, no lo que tiene que pasar.*

| Cuando | Tiene que pasar |
|---|---|
| Un socio pregunta «Según el reglamento, ¿cuánto pago de recargo si debo 3 cuotas?» | El equipo busca en el reglamento, hace la cuenta y, antes de responder, te pide que apruebes |
| La respuesta tiene un error y la rechazás | No le llega al socio |
| Querés saber qué pasó con una pregunta de ayer | En el registro ves qué consultó, cuántos tokens usó y cuánto costó |
| Un socio escribe su email en la pregunta | El email no llega al modelo ni queda en el registro |
| Un compañero instala tu asistente siguiendo tu README | Le anda sin tener que preguntarte nada |

**Qué subís.** Tu asistente terminado, con su README, una prueba automática de tu protección, el documento de arquitectura y el registro de evaluación (las plantillas están en `docs/`) y, en la tarea, el PDF de tus slides.

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
