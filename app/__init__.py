from fastapi import FastAPI
from fastapi.routing import APIRoute

from app.config import custom_settings

from magicapi import create_app, create_handler

custom_settings.app_name = custom_settings.service

app = create_app(config_settings=custom_settings)

# add imports here...
from app.Routes import example_endpoints

app.include_router(
    example_endpoints.boilerplate_router, prefix="/examples", tags=["examples"],
)

def use_route_names_as_operation_ids(app: FastAPI) -> None:
    for route in app.routes:
        if isinstance(route, APIRoute):
            route.operation_id = route.name


use_route_names_as_operation_ids(app)

handler = create_handler(app)
