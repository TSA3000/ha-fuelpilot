"""Provider registry. Each provider: async fetch(session) -> dict
{"prices": {fuel_key: float}, "valid": str | None, "source": str}"""
from . import st1

PROVIDERS = {
    "st1": ("St1 (listpris)", st1.fetch),
}
