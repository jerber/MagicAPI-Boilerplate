from magicapi import app, router, create_handler

# add imports here
from app import Routes

app.include_router(router)
handler = create_handler(app)
