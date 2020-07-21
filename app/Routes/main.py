import time
from magicapi import g
from magicapi.Decorators.background_tasks import run_in_background
from fastapi import APIRouter

# from magicapi.Utils.middleware import MagicCallLogger
from magicapi.RouteClasses import MagicCallLogger

@g.app.get("/hey")
def hey(greeting: str = "hey man"):
    return f"{greeting} !!!"


# from magicapi import magic_router
rr = APIRouter(route_class=MagicCallLogger)

@run_in_background
def sleep():
    time.sleep(0.3)


@rr.get("/yes")
def yes():
    sleep()
    return "yaaaa"


@rr.get("/yyii")
def yyii():
    sleep()
    return "yaaaa"

@g.magic_router.get('/using_magic')
def using_magic():
    return 'YEEEEEE'


# g.app.include_router(g.magic_router)
g.app.include_router(rr)
