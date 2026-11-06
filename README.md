# FuelPilot ⛽

Svenska drivmedelspriser i Home Assistant.

| Källa | Typ | Bränslen |
|---|---|---|
| St1 | Listpris (St1 Business), hela landet | Bensin 95/98, E85, Diesel, HVO100 |

> Listpris är kedjans gemensamma pris, inte pumppriset på en enskild station.

## Installation

**Marketplace (HA 2026.11+):** Inställningar → Marketplace → **Add from link** → `TSA3000/ha-fuelpilot` → Install.

**Manuellt:** kopiera `custom_components/fuelpilot` till `/config/custom_components/` och starta om.

## Sensorer

`sensor.st1_listpris_diesel` m.fl. — enhet `SEK/L`, attribut `valid_from`, `source`, `price_type`. Uppdateras varje timme.

## Författare

Sam Mahdi ([@TSA3000](https://github.com/TSA3000))