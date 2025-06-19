'''''
Question 3: Do Django signals run in the same database transaction as the caller?

Answer: Yes, unless using transaction.on_commit, signals are part of the same transaction.

'''

from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def signal_handler(sender, instance, created, **kwargs):
    print("Signal handler running")

def create_user():
    try:
        with transaction.atomic():
            User.objects.create(username="txn_test")
            raise Exception("Force rollback")
    except:
        pass
