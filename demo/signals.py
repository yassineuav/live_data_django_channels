from django.db.models.signals import post_save, post_delete, pre_delete
from django.dispatch import receiver
from demo.models import Drone


@receiver(post_save, sender=Drone)
def handle_post_save(sender, instance, created, **kwargs):
    if created:
        print("New record inserted:", instance)
    else:
        print("Record updated:", instance)


@receiver(post_delete, sender=Drone)
def handle_post_delete(sender, instance, **kwargs):
    print("Record deleted:", instance)


@receiver(pre_delete, sender=Drone)
def handle_pre_delete(sender, instance, **kwargs):
    print("About to delete record:", instance)
