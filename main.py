from magicapi import app, router, handler

# add imports here
from app import Routes

app.include_router(router)
