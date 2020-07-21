from magicapi import router
import time


@router.get("/beatgig")
def beatgig():
    return "beatgig!!!!"


@router.get('/sleep')
async def sleep(secs: int = 5):
    time.sleep(secs)
    return f'done! {secs}'
