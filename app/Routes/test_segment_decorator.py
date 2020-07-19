from magicapi import router
from magicapi.Services.Doorman import CurrentUser, GET_USER
from magicapi.Services.Segment.decorator import segment


@router.get("/segment_decorator", response_model=CurrentUser, tags=["seg"])
@segment(keywords=["current_user"])
async def get_curr_user_w_seg(current_user: CurrentUser = GET_USER):
    return current_user
