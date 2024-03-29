import os
from typing import Any, Dict, List

from pydantic.v1 import BaseSettings


class AppSettings(BaseSettings):
    app_env: str = os.getenv("ENVIRONMENT")
    debug: bool = False
    docs_url: str = "/docs"
    openapi_prefix: str = ""
    openapi_url: str = "/openapi.json"
    redoc_url: str = "/redoc"
    title: str = "Foodify_backend"
    description: str = "API to register food"
    version: str = "0.1.0"

    allowed_hosts: List[str] = ["*"]  # TODO Tienes que cambiar esto para que te permita coger las variables del .env

    api_prefix: str = "/api"

    @property
    def fastapi_kwargs(self) -> Dict[str, Any]:
        return {
            "debug": self.debug,
            "docs_url": self.docs_url,
            "openapi_prefix": self.openapi_prefix,
            "openapi_url": self.openapi_url,
            "redoc_url": self.redoc_url,
            "title": self.title,
            "description": self.description,
            "version": self.version,
        }
