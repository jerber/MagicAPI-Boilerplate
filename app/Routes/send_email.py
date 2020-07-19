from typing import List

from magicapi import router

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
