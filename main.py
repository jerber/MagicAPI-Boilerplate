from app.config import custom_settings

from magicapi import create_app, create_handler, add_magic_routers


app = create_app(config_settings=custom_settings)

# add imports here...
from app.Routes import example_boilerplate_endpoints

app.include_router(
    example_boilerplate_endpoints.boilerplate_router,
    prefix="/boilerplate",
    tags=["boilerplate"],
)

handler = create_handler(app)
add_magic_routers()  # use this if you use g.magic_router...
