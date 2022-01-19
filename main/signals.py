import json
from django.db.models.signals import post_save
from django.dispatch import receiver, Signal
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from user.models import User

order_created = Signal()

with open(settings.BASE_DIR / 'config.json') as config_file:
    config = json.load(config_file)

@receiver(post_save, sender=User)
def notify_me_of_registration(sender, instance, created, **kwargs):
    if created:
        title = 'someone has registered'
        text_message = f"someone has registered email: {instance.email}"
        from_email = config['MAIL_USERNAME']
        to_email = config['admins']
        msg = EmailMultiAlternatives(
            title, text_message, from_email, to_email)
        msg.send(fail_silently=True)


@receiver(order_created)
def notify_me_of_order_creation(sender, **kwargs):
    order = kwargs.get('order')
    title = 'someone has made an order in yourpsychedelicstore.com'
    text_message = f"{order.user.email} bought {order.cost} usd"
    from_email = config['MAIL_USERNAME']
    to_email = config['admins']
    msg = EmailMultiAlternatives(
        title, text_message, from_email, to_email)
    msg.send(fail_silently=True)

