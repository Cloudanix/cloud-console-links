import logging

from .links import Resource

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
            logger.debug(f"Invalid resource_name - {resource_name}")
            raise ValueError("Invalid parameters provided")

        return method(**kwargs).replace(" ", "")
