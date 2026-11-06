# FuelPilot ⛽

Swedish fuel prices in Home Assistant.

| Source | Type | Fuels |
|---|---|---|
| St1 | National list price (St1 Business) | Petrol 95/98, E85, Diesel, HVO100 |

> The list price is the chain's nationwide reference price, not the pump price at a specific station.

## Installation

**Marketplace (HA 2026.11+):** Settings → Marketplace → **Add from link** → `TSA3000/ha-fuelpilot` → Install.

**Manual:** copy `custom_components/fuelpilot` to `/config/custom_components/` and restart Home Assistant.

## Configuration

Settings → Devices & services → **Add integration** → **FuelPilot** → select a price source.

## Sensors

One sensor per fuel, e.g. `sensor.st1_list_price_diesel`.

| Attribute | Description |
|---|---|
| `valid_from` | Date the list price is valid from |
| `source` | URL the price was read from |
| `price_type` | `list_price` |

Unit: `SEK/L`. Updated every hour. Long-term statistics enabled.

## Removal

Settings → Devices & services → FuelPilot → ⋮ → **Delete**, then uninstall from the Marketplace.

## Author

Sam Mahdi ([@TSA3000](https://github.com/TSA3000))

## License

MIT
