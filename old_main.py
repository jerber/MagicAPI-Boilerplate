from magicapi.config import settings

settings.app_name = "breat"
settings.version = "1.0.1"
# from magicapi import app, router, handler, create_app, create_handler
from magicapi import app, create_app, create_handler, router


app = create_app(settings)

handler = create_handler(app)

# add imports here
from app import Routes

app.include_router(router)



# should be main...

'''
from x import settings

from magicapi import create_app, create_handler, add_call_to_db

# the create app already gives this app the backround stuff

app = create_app(settings) # this adds all the services included w magicdb...
handler = create_handler(app)
'''