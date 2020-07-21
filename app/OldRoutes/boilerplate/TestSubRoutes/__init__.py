from magicapi.Utils.importing import get_all_subfiles_and_dirs

from fastapi import APIRouter

# from magicapi import CallRoute
from magicapi.RouteClasses import MagicCallLogger

# from magicapi import app
from magicapi import g

sub_router = APIRouter(route_class=MagicCallLogger)

# imports all of the subroutes...
__all__ = get_all_subfiles_and_dirs(__file__)
from . import *

g.app.include_router(sub_router, prefix="/sub_routes", tags=["sub_routes_boilerplate"])
