from __future__ import annotations

from homeassistant.components.sensor import SensorEntity, SensorStateClass
from homeassistant.helpers.device_registry import DeviceEntryType, DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN, FUEL_NAMES
from .providers import PROVIDERS


async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = entry.runtime_data
    async_add_entities(
        FuelPriceSensor(coordinator, entry, fuel)
        for fuel in coordinator.data["prices"]
    )


class FuelPriceSensor(CoordinatorEntity, SensorEntity):
    _attr_has_entity_name = True
    _attr_native_unit_of_measurement = "SEK/L"
    _attr_state_class = SensorStateClass.MEASUREMENT
    _attr_suggested_display_precision = 2
    _attr_icon = "mdi:gas-station"

    def __init__(self, coordinator, entry, fuel: str) -> None:
        super().__init__(coordinator)
        self._fuel = fuel
        self._attr_name = FUEL_NAMES.get(fuel, fuel)
        self._attr_unique_id = f"{entry.entry_id}_{fuel}"
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, entry.entry_id)},
            name=PROVIDERS[coordinator.provider][0],
            manufacturer=coordinator.provider.upper(),
            entry_type=DeviceEntryType.SERVICE,
        )

    @property
    def native_value(self):
        return self.coordinator.data["prices"].get(self._fuel)

    @property
    def extra_state_attributes(self):
        d = self.coordinator.data
        return {"valid_from": d.get("valid"), "source": d.get("source"), "price_type": "listpris"}
