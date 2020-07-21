from app.config import custom_settings

from magicapi import create_app, create_handler, add_magic_routers


app = create_app(config_settings=custom_settings)

# add imports here...
from app.Routes import main
from app import OldRoutes
from app.Routes import items

app.include_router(items.router, prefix='/items', tags=['items_boi'])
handler = create_handler(app)
add_magic_routers()
