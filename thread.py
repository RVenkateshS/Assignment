'''''

Question 2: Do Django signals run in the same thread as the caller?

Answer: Yes, by default, signals run in the same thread.

'''

import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def signal_handler(sender, instance, created, **kwargs):
    print("Signal Thread:", threading.current_thread().name)

def create_user_view(request):
    print("View Thread:", threading.current_thread().name)
    User.objects.create(username="thread_test")

