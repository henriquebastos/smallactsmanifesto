from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings


def send_email_confirmation(signatory):
    context = {
        "name": signatory.name,
        "activate_url": signatory.get_confirm_url(),
        "confirmation_key": signatory.confirmation_key,
        }
    subject = render_to_string("signatures/mail_subject.txt", context)
    message = render_to_string("signatures/mail_message.txt", context)
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL,
        [signatory.email, settings.DEFAULT_FROM_EMAIL])
