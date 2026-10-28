"""Lo que tu agente usa y no hace falta que escribas (prácticas M6 a M8): from herramientas import buscar_web, calcular, Medidor
- buscar_web y calcular: dos herramientas listas. La tercera, buscar_documentos, la escribís vos en v04_agente.py:
  es la que lleva tu tema.
- Medidor: cuenta lo que pasó en una pregunta (llamadas al modelo, herramientas, documentos, tokens y segundos).

En config.toml elegís cómo busca en internet:
  web = "real"     DuckDuckGo, gratis y sin clave
  web = "grabada"  siempre la misma respuesta guardada (fixtures/web.json): sirve para medir la ELECCIÓN, sin internet
  web = "caida"    simula que la web no responde: para ver si tu agente avisa o inventa

Las dos son de solo lectura: buscan o calculan, nunca escriben ni borran.
Corré uv run python herramientas.py para ver lo que el modelo sabe de cada una.
"""

import json
import os
import re
import time
from typing import Literal

from langchain.tools import tool
from langchain_core.callbacks import BaseCallbackHandler

from llm import RAIZ, config


@tool
def buscar_web(consulta: str) -> str:
    """Busca en internet información reciente o que no está en mis documentos (noticias, precios, versiones nuevas, fechas)."""
    modo = str(os.getenv("WEB") or config().get("web", "real")).strip().lower()  # «Grabada» vale igual
    if modo not in ("real", "grabada", "caida"):  # una errata («grabado») buscaría en la web real sin avisar
        raise SystemExit(f'En config.toml, web = "{modo}": tiene que ser "real", "grabada" o "caida" (sin tilde).')
    if modo == "caida":
        return "ERROR: la búsqueda web no respondió. No inventes; decíselo al usuario."
    if modo == "grabada":
        return json.loads((RAIZ / "fixtures" / "web.json").read_text(encoding="utf-8")).get("resultado", "")
    try:
        from ddgs import DDGS
        resultados = DDGS().text(consulta, max_results=3)
        return "\n".join(f"- {r['title']}: {r['body'][:300]} ({r['href']})" for r in resultados) or "Sin resultados."
    except Exception as error:  # sin red, o DuckDuckGo limita cuando busca toda la clase a la vez
        print(f'(aviso: la búsqueda web falló: {type(error).__name__}. Si se repite, poné web = "grabada" en config.toml)')
        return f"ERROR: la búsqueda web falló ({type(error).__name__}). No inventes; decíselo al usuario."


@tool
def calcular(operacion: Literal["suma", "resta", "multiplicacion", "division", "porcentaje_cambio"],
             a: float, b: float) -> str:
    """Hace una cuenta con dos números. porcentaje_cambio = (b - a) / a * 100. Usar para cualquier cuenta."""
    resultado = {"suma": a + b, "resta": a - b, "multiplicacion": a * b,
                 "division": a / b if b else None,
                 "porcentaje_cambio": (b - a) / a * 100 if a else None}[operacion]
    if resultado is None:
        return "ERROR: división por cero. No inventes el resultado; decíselo al usuario."
    return f"{round(resultado, 4) + 0.0:.12g}"  # 15000, no 1.5e+04; + 0.0: «0», no «-0»


class Medidor(BaseCallbackHandler):
    """Mira sin tocar tu código: LangChain le avisa cada llamada al modelo y cada herramienta (un «callback»).
    Se usa así:  medidor = Medidor();  agente.invoke(..., {"callbacks": [medidor]});  medidor.resumen()
    También cuenta lo que hacen los agentes de adentro de un grafo (M7)."""

    def __init__(self):
        self.inicio, self.llamadas, self.herramientas, self.fuentes = time.perf_counter(), 0, [], []
        self.entrada = self.salida = 0
        self._nombres = {}

    def on_chat_model_start(self, serialized, messages, **kwargs):
        self.llamadas += 1

    def on_llm_end(self, response, **kwargs):
        for generacion in (g for lista in response.generations for g in lista):
            uso = getattr(getattr(generacion, "message", None), "usage_metadata", None) or {}
            self.entrada += uso.get("input_tokens", 0)
            self.salida += uso.get("output_tokens", 0)

    def on_tool_start(self, serialized, input_str, *, run_id, **kwargs):
        nombre = (serialized or {}).get("name") or kwargs.get("name", "?")
        self.herramientas.append(nombre)
        self._nombres[run_id] = nombre

    def on_tool_end(self, output, *, run_id, **kwargs):
        if self._nombres.get(run_id) == "buscar_documentos":  # cada fragmento empieza con [documento]
            self.fuentes += re.findall(r"^\[([^\]]+)\]$", str(getattr(output, "content", output)), re.M)

    def resumen(self):
        """Lo que los contratos piden medir desde v0.2, contado en esta pregunta."""
        return {"fuentes": list(dict.fromkeys(self.fuentes)), "herramientas": self.herramientas,
                "llamadas": self.llamadas, "latencia_s": round(time.perf_counter() - self.inicio, 2),
                "tokens_entrada": self.entrada, "tokens_salida": self.salida}


if __name__ == "__main__":
    print(calcular.invoke({"operacion": "porcentaje_cambio", "a": 80, "b": 100}))   # 25
    os.environ["WEB"] = "grabada"
    print(buscar_web.invoke({"consulta": "última versión de LangGraph"})[:120])
    print("\nLo que el modelo sabe de cada una (los comentarios con # no le llegan):")
    for h in (buscar_web, calcular):
        print(f"- {h.name}({', '.join(h.args)}): {h.description}")
