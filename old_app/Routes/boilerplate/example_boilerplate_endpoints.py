"""There are all boilerplate examples of using routes..."""

from magicapi import router

"""Example of background tasks."""
import time

from magicapi.Decorators.parse_objects import parse_objects
from magicapi.Decorators.background_tasks import run_in_background

from app.Models.TestUser import TestUser


@run_in_background
@parse_objects
def sleep_for_five(secs: float, test_user: TestUser = None):
    print("starting to sleep for test user", test_user)
    if not test_user:
        TestUser(name="Jon", age=3)
    time.sleep(secs)
    test_user.slept = True
    test_user.save(merge=True)
    print("ended sleep for test user", test_user)


@router.post("/test_async_with_firestore", tags=["boilerplate"])
def test_async(*, secs: float = 5, test_user: TestUser):
    task_id = sleep_for_five(secs, test_user)
    return {"task_id": task_id}


@router.post("/test_async_without_firestore", tags=["boilerplate"])
def test_async(*, secs: float = 5):
    task_id = sleep_for_five(secs)
    return {"task_id": task_id}


"""Example of auth."""

from magicapi.Services.Doorman import CurrentUser, GET_USER


@router.get("/get_current_user", response_model=CurrentUser, tags=["boilerplate"])
def get_current_user(current_user: CurrentUser = GET_USER):
    print(current_user)
    return current_user


"""Adding to DynamoDB Table."""

from magicapi.Models.Task import Task
from fastapi.encoders import jsonable_encoder
from typing import List


@router.post("/test_dynamo", tags=["boilerplate"])
def test_dynamo(tasks: List[Task]):
    start = time.time()
    with Task.get_table().batch_writer() as batch:
        for task in tasks:
            batch.put_item(Item=jsonable_encoder(task))
    time_took = time.time() - start

    return {"task_ids": [task.task_id for task in tasks], "time_took": time_took}


"""Errors example."""

from app.Errors.TestError import TestError


@router.get("/test_errors", tags=["boilerplate"])
def test_errors():
    raise TestError(message="This test worked!")


from fastapi import File, UploadFile


@router.post("/test_file", tags=["boilerplate"])
def test_file(file: bytes = File(...)):
    print(str(file)[100])
    return len(file)


@router.post("/test_upload_file", tags=["boilerplate"])
def test_file(file: UploadFile = File(...)):
    print("filename", file.filename)
    return "sheesh"


"""Sending to segment example and test."""

from magicapi.Services.Segment import analytics
from magicapi.Services import Segment


@router.post("/test_segment", tags=["boilerplate"])
def test_segment(id: str, action, body: dict):
    Segment.track(id, action, body)
    return "done!"


@router.post("/test_segment_without_background", tags=["boilerplate"])
def test_segment(id: str, action, body: dict):
    analytics.track(id, action, body)
    return "done!"


"""Query Params Example"""


@router.get("/query_params_test", tags=["boilerplate"])
def query_params(name: str):
    return f"hello {name}"


"""Twilio Example"""

from magicapi.Services.Twilio import send_text
from magicapi.FieldTypes import PhoneNumber
from fastapi import APIRouter

# example for using new router too
r = APIRouter()


@r.get("/send_text")
def send_text_router(phone_number: PhoneNumber, body: str):
    sid = send_text(to=phone_number, body=body)
    return sid


from magicapi import app

app.include_router(r, prefix="/text", tags=["boilerplate"])

# from app.magicapi.Services.Email import send_email_in_background
from magicapi.Services.Mailgun import send_email as send_email_mailgun


@router.post("/send_email", tags=["boilerplate"])
def send_email(*, subject: str = None, email_body: str, recipients: List[str]):
    # return send_email_in_background(text_body=body, recipients=recipients)
    res = send_email_mailgun(text=email_body, recipients=recipients, subject=subject)
    return res.content


from magicapi.Services.MagicLink import send_magic_link_email


@router.post("/send_magic_link", tags=["magic_link"])
def send_magic_link(email_address: str, redirect_url: str):
    res = send_magic_link_email(send_email_mailgun, email_address, redirect_url)
    return res.json()


from magicapi.Services.Segment.decorator import segment


@router.get("/segment_decorator", response_model=CurrentUser, tags=["seg"])
@segment(keywords=["current_user"])
async def get_curr_user_w_seg(current_user: CurrentUser = GET_USER):
    return current_user
