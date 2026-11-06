from __future__ import annotations

from homeassistant.components.sensor import SensorEntity, SensorStateClass
from homeassistant.helpers.device_registry import DeviceEntryType, DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN


async def async_setup_entry(hass, entry, async_add_entities):
    coordinator = entry.runtime_data
    async_add_entities(
        FuelPriceSensor(coordinator, entry, fuel) for fuel in coordinator.data["prices"]
    )


class FuelPriceSensor(CoordinatorEntity, SensorEntity):
    """One sensor per fuel type."""

    _attr_has_entity_name = True
    _attr_native_unit_of_measurement = "SEK/L"
    _attr_state_class = SensorStateClass.MEASUREMENT
    _attr_suggested_display_precision = 2
    _attr_icon = "mdi:gas-station"

    def __init__(self, coordinator, entry, fuel: str) -> None:
        super().__init__(coordinator)
        self._fuel = fuel
        self._attr_translation_key = fuel
        self._attr_unique_id = f"{entry.entry_id}_{fuel}"
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, entry.entry_id)},
            name=coordinator.display_name,
            manufacturer=coordinator.manufacturer,
            entry_type=DeviceEntryType.SERVICE,
        )

    @property
    def native_value(self):
        return self.coordinator.data["prices"].get(self._fuel)

    @property
    def extra_state_attributes(self):
        data = self.coordinator.data
        return {
            "valid_from": data.get("valid"),
            "source": data.get("source"),
            "price_type": "list_price",
        }
