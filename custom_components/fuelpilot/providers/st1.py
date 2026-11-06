"""St1 Sverige national list price, parsed from st1.se/foretag/listpris."""
from __future__ import annotations

import html as _html
import re

from aiohttp import ClientSession, ClientTimeout

URL = "https://st1.se/foretag/listpris"
_MAP = {
    "Bensin 95": "bensin_95",
    "Bensin 98": "bensin_98",
    "E85": "e85",
    "Diesel": "diesel",
    "HVO100": "hvo100",
}
_TAG = re.compile(r"<[^>]+>")
_PRICE = re.compile(r"(Bensin 98|Bensin 95|E85|Diesel|HVO100)\s*\|?\s*(\d{1,2},\d{2,3})\s*kr")
_VALID = re.compile(r"Listpriser gällande\s+(\d{1,2}\s+\w+\.?\s+\d{4})")


def parse(raw: str) -> dict:
    text = _html.unescape(_TAG.sub(" ", raw)).replace("\xa0", " ")
    text = re.sub(r"\s+", " ", text)
    prices: dict[str, float] = {}
    for name, value in _PRICE.findall(text):
        # first table on the page = St1-stationer; keep first hit per fuel
        prices.setdefault(_MAP[name], float(value.replace(",", ".")))
    if not prices:
        raise ValueError("No prices found on st1.se – page layout changed?")
    m = _VALID.search(text)
    return {"prices": prices, "valid": m.group(1) if m else None, "source": URL}


async def fetch(session: ClientSession) -> dict:
    async with session.get(
        URL,
        timeout=ClientTimeout(total=30),
        headers={"User-Agent": "HomeAssistant-FuelPilot/0.1"},
    ) as resp:
        resp.raise_for_status()
        return parse(await resp.text())
