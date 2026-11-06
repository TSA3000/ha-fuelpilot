from __future__ import annotations

import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .const import CONF_PROVIDER, DOMAIN, UPDATE_INTERVAL
from .providers import PROVIDERS

_LOGGER = logging.getLogger(__name__)
PLATFORMS = [Platform.SENSOR]


class FuelCoordinator(DataUpdateCoordinator[dict]):
    """Fetches prices from the configured provider."""

    def __init__(self, hass: HomeAssistant, entry: ConfigEntry) -> None:
        super().__init__(
            hass,
            _LOGGER,
            config_entry=entry,
            name=f"{DOMAIN}_{entry.data[CONF_PROVIDER]}",
            update_interval=UPDATE_INTERVAL,
        )
        self.provider = entry.data[CONF_PROVIDER]
        self.display_name, self.manufacturer, self._fetch = PROVIDERS[self.provider]

    async def _async_update_data(self) -> dict:
        try:
            return await self._fetch(async_get_clientsession(self.hass))
        except Exception as err:  # noqa: BLE001
            raise UpdateFailed(f"{self.provider}: {err}") from err


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    coordinator = FuelCoordinator(hass, entry)
    await coordinator.async_config_entry_first_refresh()
    entry.runtime_data = coordinator
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
