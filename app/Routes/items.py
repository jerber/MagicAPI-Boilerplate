from fastapi import APIRouter
from magicapi import g
from magicapi.RouteClasses import MagicCallLogger

items_arr = ['1', '4']


@g.magic_router.get('/items')
def items():
    return items_arr


router = APIRouter(route_class=MagicCallLogger)


@router.get('/itemsHURRR')
def items_hurr():
    return items_arr
