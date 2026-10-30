# Presentación — [nombre del sistema] (20 minutos, unas 10 slides)

Una idea por slide. El título de cada slide es **una frase con tu conclusión**
(«Con fragmentos de 400 apareció el documento correcto»), no un tema
(«Fragmentos»). Abajo, la evidencia: una tabla, un gráfico o una captura.

| Parte | Min | Slides | Qué va |
|---|---:|---:|---|
| 1. Contexto | 2 | 1 | Qué pregunta responde tu sistema, para quién y con qué documentos. |
| 2. Demo en vivo | 3 | 1 | Las 3 consultas que vas a correr y qué requisito muestra cada una: entre las tres, los 4 requisitos de la consigna (RAG, agente con herramientas, equipo con aprobación y tu práctica de producción). Una que sea un caso límite: sin respuesta en tus documentos (¿lo reconoce o inventa?) o con la web caída (¿avisa?). |
| 3. Arquitectura y decisiones | 5 | 3 | El diagrama del grafo. Dos o tres decisiones, cada una con la alternativa que descartaste y el número que la sostiene. |
| 4. Evaluación y límites | 5 | 3 | Tu suite: sin RAG vs con RAG, selección de herramientas, agente solo vs equipo. Un fallo clasificado. Qué no funciona todavía. |
| 5. Producción y go / no-go | 5 | 2 | Tu práctica de producción con su evidencia (traza, costo por mes, test). ¿Lo liberarías? ¿Por qué? |

**El diagrama en la slide:** Google Slides y PowerPoint no dibujan Mermaid. Pegá tu dibujo en
[mermaid.live](https://mermaid.live) (como en la práctica M7, paso 3) y, abajo a la izquierda, en **Actions**:
**PNG** baja la imagen y **Copy Image** la copia para pegarla. Si al entrar aparece un aviso para probar
la versión paga, cerralo con «Stay on mermaid.live»: el editor es gratis.

**Antes de la clase:** poné las 3 consultas en la demo de tu `v10_produccion.py` (el bloque del final; pedile a tu
asistente que corra una lista) y corré `uv run python v10_produccion.py`. Muestra la respuesta, las herramientas y el
costo, y deja la traza. Para la aprobación (requisito 3), la demo de tu `v05_equipo.py` responde la misma pregunta
aprobando y rechazando: `uv run python v05_equipo.py`, con tu pregunta en la demo. Guardá capturas por si algo
falla en vivo. Tomale el tiempo: en las pruebas del 17/10 (Gemini 3.5 Flash-Lite), una pregunta al
equipo tardó 6 s de mediana (sin contar las que dieron error: suman los reintentos), pero una tardó 134 s, y `v05_equipo.py` corre el
equipo dos veces. Si en el ensayo pasa de un minuto, en vivo mostrá esa consulta con la captura.
Cuántas llamadas gasta el ensayo lo dice la columna `llamadas` de tu medición (el equipo hace varias por pregunta):
entra varias veces en la cuota del día (500), pero no lo repitas sin motivo el día de la defensa.

**La web en la demo:** `web = "real"` en `config.toml`. Si tu caso límite es la
web caída, cambiá a `"caida"` solo para esa consulta y volvé a `"real"`. Si en
vivo falla la búsqueda de verdad, pasá a `"grabada"` y decilo (guía de la clase 8). La
grabada trae datos de LangGraph y chromadb, no de tu tema: para la respuesta de esa
consulta, mostrá la captura que guardaste.

**El PDF:** hacé las slides donde quieras y exportalas. Google Slides: *Archivo →
Descargar → Documento PDF*. PowerPoint (Windows): *Archivo → Exportar → Crear documento PDF/XPS → Crear PDF/XPS → Publicar*;
en Mac, *Archivo → Exportar* y elegí PDF en el formato (PowerPoint para Mac no conserva los enlaces en el PDF:
si tus slides tienen enlaces, por ejemplo al repo, exportalo desde PowerPoint en la web).
