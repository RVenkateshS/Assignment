'''''
Question 1: Are Django signals executed synchronously or asynchronously by default?
Answer: By default, Django signals are synchronous—they 
execute right after the signal is sent.

'''''
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import time

@receiver(post_save, sender=User)
def signal_handler(sender, instance, created, **kwargs):
    print("Signal received")
    time.sleep(5)
    print("Signal processing done")

# In your view or script
def create_user_view(request):
    User.objects.create(username="testuser")
    print("User creation done")
    
    

'''''
Expected Output :

Signal received
Signal processing done
User creation done

'''