# evidencia

Una página por versión (`m1.md`, `v0.1.md`, `v0.2.md`…). Cada una dice:

- **Qué cambiaste** y por qué.
- **Qué predijiste** antes de correr.
- **Resultado:** la tabla con las mismas preguntas, contra la versión anterior.
- **Decisión y límite:** qué te quedás y qué todavía no detecta.
- **Uso de IA:** qué te dio, qué aceptaste, corregiste o rechazaste.

Las preguntas que cada entrega pide responder están en la [consigna](../CONSIGNA.md).

## Un ejemplo, abreviado

Inventado, para ver la forma: tus números salen de tus corridas. Se escribe en Markdown (`#` para títulos, `|` para tablas) y
GitHub lo muestra con formato.

```markdown
# v0.1

**Qué cambié:** pasé de unas instrucciones genéricas a unas con los horarios y las fechas de la cooperativa.

**Qué predije:** que con esos datos iba a responder bien 4 de mis 5 preguntas.

| Configuración | Tokens de salida (promedio) | Latencia (mediana) | Buenas |
|---|---|---|---|
| A: instrucciones genéricas | 62 | 1,4 s | 2/5 |
| B: con horarios y fechas | 48 | 1,2 s | 5/5 |

**Decisión y límite:** me quedo con B. Si le pregunto algo que no le di (el precio de la cuota), inventa.

**Uso de IA:** le pedí a mi asistente el bucle que guarda cada llamada; no anotaba los errores y lo corregí.
```
