"""¿Tu entorno funciona? Uso: uv run python check_setup.py  [--model proveedor:modelo]  [--fixture]"""

import json
import subprocess
import sys
import time

from llm import RAIZ, ModeloMalEscrito, cargar_modelo, config, explicar, falta_clave, nombre_modelo, sin_claves  # noqa: F401  (falta_clave: la usan los tests)

PREGUNTA = "Respondé en una frase: ¿qué es un token en un modelo de lenguaje?"


def clave_protegida():
    """sí / NO / un aviso si no se puede comprobar (git sin instalar o carpeta bajada como ZIP)."""
    try:
        r = subprocess.run(["git", "check-ignore", "-q", str(RAIZ / ".env")], capture_output=True)
    except FileNotFoundError:
        # GitHub Desktop trae su propio git, pero no lo deja disponible en la terminal
        return "no se pudo comprobar: la terminal no encuentra git. Mirá en GitHub Desktop que .env no aparezca en Changes"
    return {0: "sí", 1: "NO — revisá .gitignore antes de commitear"}.get(
        r.returncode, "no se pudo comprobar: esta carpeta no es un repo git (clonala con GitHub Desktop)")


if __name__ == "__main__":
    # «--fixtures» o «—fixture» (Word cambia -- por una raya) se ignoraban y pedía la clave que --fixture saltea
    otras = [a for a in sys.argv[1:] if a[:1] in "-—–" and a not in ("--fixture", "--model")]
    if otras:
        raise SystemExit(f"No conozco «{otras[0]}». Las opciones son --fixture (sin clave) y --model, "
                         "con dos guiones comunes: uv run python check_setup.py --fixture")
    if "--fixture" in sys.argv:
        f = json.loads((RAIZ / "fixtures" / "check_setup.json").read_text(encoding="utf-8"))
        print(f"[FIXTURE — no prueba tu conexión] {f['respuesta']}\nuso: {f['usage']}")
        sys.exit(0)

    if sys.argv[-1] == "--model":  # sin el nombre, cortaba con un IndexError en inglés
        raise SystemExit("Después de --model va el modelo: uv run python check_setup.py --model google_genai:gemini-3.5-flash-lite")
    modelo = nombre_modelo(sys.argv[sys.argv.index("--model") + 1] if "--model" in sys.argv else None)
    print(f"modelo: {modelo}")
    print(f".env ignorado por git: {clave_protegida()}")
    web = str(config().get("web", "real")).strip().lower()  # como buscar_web: «Real» vale igual
    if web != "real":  # «grabada» o «caida» sirven para medir y probar (M6–M8); la entrega va con la real (README)
        print(f'OJO: web = "{web}" en config.toml. Para usarlo de verdad y para entregar, va "real".')
    t0 = time.perf_counter()
    try:
        r = cargar_modelo(modelo).invoke(PREGUNTA)
    except ModeloMalEscrito as error:  # el aviso de llm.py: entero, con su «¿Quisiste decir…?», sin pistas de clave
        print(error)
        sys.exit(1)
    except Exception as error:  # un mensaje claro en vez de un error largo de Python
        print(f"ERROR al llamar al modelo: {type(error).__name__}: {sin_claves(str(error))[:200]}")
        if modelo.startswith("ollama:"):  # local: no hay clave; lo habitual es que Ollama no esté abierto
            print("Pistas: ¿Ollama está abierto? (abrí la app o corré «ollama serve»). ¿Bajaste el modelo con «ollama pull»?")
        elif explicar(error):  # cuota, red, clave rechazada o proveedor saturado: ya se sabe cuál, sin adivinar
            print(explicar(error))
        else:
            print("Pistas: la clave está mal copiada (va completa, después del = y en el mismo renglón de .env), el modelo está mal escrito en config.toml,")
            print("o no hay internet.")
        print("Mientras tanto podés seguir con --fixture.")
        sys.exit(1)
    print(f"respuesta: {r.text.strip()}")
    print(f"uso: {r.usage_metadata}  latencia: {time.perf_counter() - t0:.1f}s")
    # el buscador de la clase 3 usa un modelo de embeddings local (unos 80 MB): mejor bajarlo ahora
    # que en el aula, todos a la vez por el mismo Wi-Fi. Ya bajado, tarda unos segundos.
    print("embeddings de Chroma (la primera vez se bajan unos 80 MB): ", end="", flush=True)
    try:
        from chromadb.utils.embedding_functions import DefaultEmbeddingFunction
        DefaultEmbeddingFunction()(["hola"])
        print("listos")
    except Exception as error:  # sin internet no es grave: se bajan solos la primera vez que se usen
        print(f"no se pudieron bajar ({type(error).__name__}); se bajan solos la primera vez que los uses (clase 3)")
    print("OK: entorno listo.")
