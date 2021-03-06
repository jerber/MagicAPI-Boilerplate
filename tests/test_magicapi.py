from magicapi import __version__


def test_version():
    assert __version__ == "0.1.0"


import time
import os

import requests

from start import use_host, port

from magicapi.app_factory import create_app

app = create_app()
from magicapi import g

example_prefix = "/examples"

# first start the sever w ./start
base_url = f"http://{use_host}:{port}"
# are you using real url and real db?

# RUNNING NON LOCALLY NOW... just put in the url you want to run here.... will use defualt db
if os.getenv("aws") or False:
    real_url = f"https://jeremyberman.org/dev"
    base_url = real_url

if os.getenv('testing_url'):
    real_url = os.getenv('testing_url')
    base_url = real_url


def test_root():
    response = requests.get(base_url + "/")
    assert response.status_code == 200


def test_test_errors():
    valid_response = {"success": False, "message": "This test worked!"}
    response = requests.get(base_url + f"{example_prefix}/test_errors")
    print(response.json())
    assert response.status_code == 452
    assert response.json() == valid_response


def test_background_tasks_via_call():
    from magicapi.Models.Call import Call
    from magicapi.Utils.random_utils import random_str

    code = random_str(30)
    url = f"{base_url}{example_prefix}/test_errors?{code}=yes"
    response = requests.get(url=url)
    assert response.status_code == 452
    time.sleep(5)  # give time to write to DB
    calls = Call.collection.where("request.url", "==", url).stream()
    assert len(calls) == 1
