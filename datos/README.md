# datos

Tus entradas y tus preguntas de prueba, una por línea en JSON (`.jsonl`).

- `m2_textos.jsonl`: los 10 textos de la práctica M2, cada uno con su `entidad` y su `cifra` esperadas.
- `m4_suite.jsonl`: 13 preguntas de prueba sobre los documentos de ejemplo de `corpus/` (práctica M4). En `fuentes`, el
  documento que tiene la respuesta (sin extensión); vacío si la respuesta no está. Tu suite, `mi_suite.jsonl`, va igual.

Por ejemplo:

```json
{"pregunta": "¿Qué plazo tiene el trámite?", "esperada": "30 días"}
```
