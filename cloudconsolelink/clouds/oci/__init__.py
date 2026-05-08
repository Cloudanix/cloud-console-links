import logging

from .links import Resource, SERVICE_HOME_MAP

logger = logging.getLogger(__name__)


class OCILinker:
    def get_console_link(
        self,
        resource_name: str = "",
        **kwargs,
    ) -> str:
        if not resource_name:
            logger.debug("resource_name is required")
            raise ValueError("Invalid parameters provided")

        resource = Resource()
        method = getattr(resource, resource_name, None)

        if method is None or resource_name.startswith("_") or not callable(method):
            home_name = SERVICE_HOME_MAP.get(resource_name)
            if home_name:
                home_method = getattr(resource, home_name, None)
                if home_method and callable(home_method):
                    logger.debug(f"resource_name {resource_name!r} not found, falling back to {home_name!r}")
                    return home_method(**kwargs).replace(" ", "")
            logger.debug(f"Invalid resource_name - {resource_name}")
            raise ValueError("Invalid parameters provided")

        return method(**kwargs).replace(" ", "")
