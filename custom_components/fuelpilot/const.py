from datetime import timedelta

DOMAIN = "fuelpilot"
CONF_PROVIDER = "provider"
UPDATE_INTERVAL = timedelta(hours=1)

FUEL_NAMES = {
    "bensin_95": "Bensin 95",
    "bensin_98": "Bensin 98",
    "e85": "E85",
    "diesel": "Diesel",
    "hvo100": "HVO100",
}
