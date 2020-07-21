from magicapi import g
import time


@g.magic_router.get("/beatgig")
def beatgig():
    return "beatgig!!!!"


@g.magic_router.get('/sleep')
async def sleep(secs: int = 5):
    time.sleep(secs)
    return f'done! {secs}'
