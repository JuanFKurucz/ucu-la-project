"""Crea el modelo configurado en config.toml.

Para probar otro modelo, cambiá la línea model de config.toml.
(La variable de entorno MODELO, si existe, tiene prioridad: la usan los tests.)
"""

import os
import re
import sys
import tomllib
from pathlib import Path

import httpx
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

RAIZ = Path(__file__).resolve().parent
load_dotenv(RAIZ / ".env")  # nunca imprimir el entorno: tiene tu clave
# En Windows, con la salida a un archivo (> salida.txt), «→» o «✓» cortaban el programa: mejor un «?»
for _flujo in (sys.stdout, sys.stderr):
    if hasattr(_flujo, "reconfigure"):
        _flujo.reconfigure(errors="replace")


def explicar_429(error):
    """Un 429 en una línea, igual en todos los programas; None si no es un 429 (ese error conviene verlo entero)."""
    texto = str(error)  # entero: en Gemini, «PerDay» aparece cerca del carácter 950
    if "429" not in texto and "RESOURCE_EXHAUSTED" not in texto:
        return None
    if "perday" in texto.lower().replace(" ", ""):  # Gemini: «PerDay» o «per day»
        return ("429: se terminó la cuota del día de ese modelo. Reintentar no sirve: "
                "esperá a mañana o cambiá de modelo en config.toml (guía 2).")
    return "429: demasiados pedidos por minuto. Esperá un minuto y corré de nuevo (guía 2)."


def explicar_sin_saldo(error):
    """Cuenta sin saldo o con el límite de gasto: esperar no lo arregla. None si no es eso."""
    texto = str(error)  # OpenAI: un 429 con estos códigos; Anthropic: 402 «billing_error»; Gemini: 402 PAYMENT_REQUIRED (documentación)
    if any(c in texto for c in ("insufficient_quota", "credit_balance_exhausted", "spend_limit_exceeded",
                                "usage_limit_exceeded", "billing_error", "PAYMENT_REQUIRED")):
        return ("Tu cuenta del proveedor no tiene saldo o llegó a su límite de gasto. Esperar no sirve: "
                "cargá saldo o volvé al modelo del curso en config.toml (guía 2).")
    return None


def explicar_sin_conexion(error):
    """Sin internet (el wifi del aula): una línea; None si no es eso. Busca en la cadena de causas del error."""
    while error is not None:
        if isinstance(error, (httpx.ConnectError, httpx.ConnectTimeout)):
            return (f"Sin conexión con el proveedor del modelo ({type(error).__name__}): revisá internet y corré de nuevo. "
                    "Mientras, sin red andan los tests y lo que no llama al modelo.")
        error = error.__cause__ or error.__context__
    return None


def explicar_clave_rechazada(error):
    """La clave existe pero el proveedor la rechaza (mal copiada, borrada o cambiada): una línea; None si no es eso."""
    texto = str(error)  # Gemini, OpenAI y Anthropic lo dicen distinto
    if any(f in texto for f in ("API key not valid", "API_KEY_INVALID", "Incorrect API key", "invalid x-api-key",
                                "PERMISSION_DENIED")):  # Gemini 403: la clave no tiene permiso (documentación de errores)
        return ("El proveedor rechazó la clave de .env: está mal copiada o ya no vale. Revisala o sacá una nueva "
                "(guía 1, «Si te trabás»; si la cambiaste por seguridad, guía 8).")
    return None


def explicar_saturado(error):
    """El proveedor está saturado (503 de Gemini y OpenAI, «overloaded» de Anthropic): una línea; None si no es eso."""
    texto = str(error)  # Gemini: «503 UNAVAILABLE … high demand» (medido el 19/10 con gemini-3.1-flash-lite)
    if any(f in texto for f in ("503 UNAVAILABLE", "high demand", "overloaded")):
        return ("503: el proveedor está saturado; no es tu código ni tu cuota. Esperá un minuto y corré de nuevo; "
                "si sigue, cambiá de modelo en config.toml (guía 2).")
    return None


def explicar_falla_del_proveedor(error):
    """Un 500 o un 504 del proveedor: pasajero, se reintenta (documentación de errores de Gemini). None si no es eso."""
    texto = str(error)
    if any(f in texto for f in ("500 INTERNAL", "504 DEADLINE_EXCEEDED")):
        return ("Falla del lado del proveedor (500 o 504): no es tu código ni tu clave. Esperá un minuto y corré "
                "de nuevo; si sigue, cambiá de modelo en config.toml (guía 2).")
    return None


def explicar_modelo_inexistente(error):
    """Un 404: el nombre del modelo no existe (una letra de menos) o, en Ollama, no lo bajaste. None si no es eso."""
    texto = str(error)  # Gemini: «404 NOT_FOUND»; Ollama: «not found (status code: 404)» (medidos en logs/v01.jsonl)
    if any(f in texto for f in ("404 NOT_FOUND", "status code: 404", "model_not_found", "not_found_error")):
        return ("404: ese modelo no existe con ese nombre. Revisá `model` en config.toml letra por letra "
                "(guiones y puntos incluidos); con Ollama, bajalo antes con «ollama pull». Reintentar no sirve.")
    return None


def explicar(error):
    """Un error conocido en una línea: sin saldo, cuota (429), red, clave, proveedor saturado o con una falla
    pasajera (500, 503, 504) y modelo inexistente (404). None si no es uno de esos: ese conviene verlo entero."""
    return (explicar_sin_saldo(error) or explicar_429(error) or explicar_sin_conexion(error) or explicar_clave_rechazada(error)
            or explicar_saturado(error) or explicar_falla_del_proveedor(error)
            or explicar_modelo_inexistente(error))


def _sin_traza_si_se_explica(tipo, error, traza):
    # v02 a v10 no atajan errores: un 429, una caída de red o una clave rechazada salían como 40 renglones en inglés
    mensaje = explicar(error)
    if mensaje:
        print(mensaje, file=sys.stderr)
    else:
        sys.__excepthook__(tipo, error, traza)


sys.excepthook = _sin_traza_si_se_explica


def sin_claves(texto):
    """Tapa lo que parezca una clave en un mensaje de error: esos textos van a logs/, a la suite y a tu evidencia."""
    return re.sub(r"(AIza[0-9A-Za-z_\-]{20,}|sk-[A-Za-z0-9_\-*.]{16,})", "[clave tapada]", texto)


def pista_json(linea):
    """Para un renglón JSON que no se lee: el porqué más común, en castellano (o "" si no se reconoce)."""
    if any(c in linea for c in "“”"):  # Word, Docs y el Editor de Texto de Mac cambian " por “ ”: se ven bien
        return ' Tiene comillas curvas “ ”: cambialas por rectas " (escribilas en VS Code).'
    if linea.rstrip().endswith(","):  # copiado de una lista [ {…}, {…} ]
        return " Sobra la coma al final del renglón: borrala."
    if linea.lstrip().startswith("{'"):  # como un diccionario de Python
        return ' Las comillas van dobles: "id", no \'id\'.'
    return ""


def config():
    # utf-8-sig: también acepta el «UTF-8 con BOM» del Bloc de notas (con utf-8 daba «Invalid statement»)
    texto = (RAIZ / "config.toml").read_text(encoding="utf-8-sig")
    try:
        return tomllib.loads(texto)
    except tomllib.TOMLDecodeError as error:  # lo más común: faltan las comillas, o un decimal con coma
        curvas = ' Tiene comillas curvas “ ”: cambialas por rectas ".' if any(c in texto for c in "“”") else ""
        raise SystemExit(f'config.toml está mal escrito ({error}). Los textos van entre comillas: web = "grabada"; '
                         f'los decimales, con punto: temperature = 0.5.{curvas}')


# Tope de tokens de salida: cada proveedor lo llama distinto.
TOPE = {"openai": "max_tokens", "anthropic": "max_tokens", "google_genai": "max_output_tokens", "ollama": "num_predict"}
# Se mira la variable, no el archivo: la clave puede venir de .env o del sistema (y un .env puede no tenerla).
# El nombre sin proveedor, como aparece en la página de cada empresa: cuál le corresponde.
PREFIJOS = {"gemini": "google_genai", "gpt": "openai", "claude": "anthropic", "qwen": "ollama"}
CLAVES = {"google_genai": ("GOOGLE_API_KEY", "GEMINI_API_KEY"), "openai": ("OPENAI_API_KEY",),
          "anthropic": ("ANTHROPIC_API_KEY",)}


class ModeloMalEscrito(SystemExit):
    """Proveedor mal escrito: corta con un aviso de una línea, no con un error largo de Python."""


def falta_clave(modelo):
    """El nombre de la variable de la clave si falta; None si está o si el proveedor no la pide (Ollama)."""
    variables = CLAVES.get(modelo.split(":")[0], ())
    return variables[0] if variables and not any(os.getenv(v) for v in variables) else None


# Google dejó de usar la temperatura en estos modelos: la aceptan y la ignoran.
# shortcut: es la lista de LangChain (10/2026); si Google suma modelos, agregalos acá.
IGNORAN_TEMPERATURA = ("gemini-3.5-flash-lite", "gemini-3.6-flash")


def usa_temperatura(model):
    """¿Le llega la temperatura a este modelo? Solo a Ollama y a Gemini (salvo los de arriba)."""
    prov, _, nombre = "".join(model.split()).partition(":")  # como nombre_modelo: «google_genai: x» vale igual
    return prov == "ollama" or (prov == "google_genai" and nombre not in IGNORAN_TEMPERATURA)


def nombre_modelo(model=None):
    """El modelo que se va a usar: el que pasás, o MODELO, o el de config.toml."""
    return "".join((model or os.getenv("MODELO") or config()["model"]).split())  # «google_genai: x» → sin espacios: ningún modelo los lleva


def cargar_modelo(model=None, temperature=None, max_salida=None):
    c = config()
    model = nombre_modelo(model)
    temperature = c.get("temperature", 0.0) if temperature is None else temperature
    prov = model.split(":")[0]
    if prov not in TOPE:  # un nombre mal escrito daría un error críptico más adelante
        pista = next((f" ¿Quisiste decir {p}:{model}?" for inicio, p in PREFIJOS.items() if model.startswith(inicio)), "")
        parecido = prov.lower() if prov.lower() in TOPE else {"google": "google_genai", "gemini": "google_genai"}.get(prov.lower())
        if not pista and parecido:  # «Google_GenAI:…» o «google:…»: casi bien
            pista = f" ¿Quisiste decir {parecido}:{model.partition(':')[2]}?"
        raise ModeloMalEscrito(f"Modelo mal escrito: proveedor «{prov}» no usado en el curso. Escribí proveedor:modelo con uno de: {', '.join(TOPE)}.{pista}")
    if falta_clave(model):  # sin esto, el proveedor corta con un error largo en inglés
        # Windows esconde las extensiones: al copiar, el archivo suele quedar como .env.txt y no se lee
        txt = (" Hay un .env.txt: Windows le agregó «.txt» al nombre. Renombralo a .env (Explorador: "
               "Ver → Extensiones de nombre de archivo, para ver el nombre entero).") if (RAIZ / ".env.txt").exists() else ""
        variable = falta_clave(model)
        if (RAIZ / ".env").exists():  # lo copió, pero el renglón no se lee: «GOOGLE_API_KEY: …» o la clave sola
            raise SystemExit(f"Falta la clave {variable} para {model}: tu .env existe, pero no tiene el renglón "
                             f"{variable}=tu-clave (el nombre, un = y la clave pegada, sin espacios en el medio). "
                             "Después: uv run python check_setup.py")
        raise SystemExit(f"Falta la clave {variable} para {model}: copiá .env.example como .env y pegá "
                         f"tu clave ahí (hoja del entorno guiado de la clase 1, paso 4). Después: uv run python check_setup.py{txt}")
    clave = next((os.getenv(v) for v in CLAVES.get(prov, ()) if os.getenv(v)), "")
    if any(c in clave for c in "“” \t"):  # se carga tal cual y el proveedor la rechaza como «mal copiada»
        raise SystemExit(f"La clave de {model} tiene un espacio en el medio o comillas curvas “ ”: en .env, borralos "
                         "(las comillas rectas \" no molestan). Después: uv run python check_setup.py")
    tope = max_salida or c.get("max_salida", 300)
    if isinstance(tope, bool) or not isinstance(tope, int) or tope < 1:  # «1.000» llegaba como 1 token, sin aviso
        raise SystemExit(f"max_salida = {tope!r} en config.toml: va un entero, sin punto de miles ni comillas "
                         "(max_salida = 300).")
    extra = {TOPE[prov]: tope}
    if usa_temperatura(model):  # gpt-5.x y claude-*-5-5 la rechazan; Gemini 3.5 Flash-Lite la ignora
        extra["temperature"] = temperature
    if prov == "ollama":
        extra["reasoning"] = False  # qwen3.5 "piensa" por defecto
    return init_chat_model(model, **extra)
