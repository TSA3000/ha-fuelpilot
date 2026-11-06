from __future__ import annotations

import voluptuous as vol
from homeassistant.config_entries import ConfigFlow

from .const import CONF_PROVIDER, DOMAIN
from .providers import PROVIDERS


class FuelPilotConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            await self.async_set_unique_id(user_input[CONF_PROVIDER])
            self._abort_if_unique_id_configured()
            return self.async_create_entry(
                title=PROVIDERS[user_input[CONF_PROVIDER]][0], data=user_input
            )
        schema = vol.Schema(
            {vol.Required(CONF_PROVIDER, default="st1"): vol.In(
                {k: v[0] for k, v in PROVIDERS.items()})}
        )
        return self.async_show_form(step_id="user", data_schema=schema)
