"""Provider registry.

Each provider exposes: async fetch(session) -> dict
    {"prices": {fuel_key: float}, "valid": str | None, "source": str}
"""
from . import st1

# key: (display name, manufacturer, fetch function)
PROVIDERS = {
    "st1": ("St1 (list price)", "St1", st1.fetch),
}
