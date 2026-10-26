"""Tu primera prueba: el proyecto lee config.toml. Corré: uv run pytest"""
from llm import config


def test_config_tiene_modelo():
    assert ":" in config()["model"]  # formato proveedor:modelo
