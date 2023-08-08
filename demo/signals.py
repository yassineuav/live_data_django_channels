import asyncio
import threading
import time
from itertools import cycle

from django.db.models.signals import post_save, post_delete, pre_delete, m2m_changed
from django.dispatch import receiver

from demo.models import Order, Drone, OrderStatus


# if the status pending
# check the weight if the wight < 50 and last update < 2 minutes
# else return notification to admin dashboard weight is to heavy
#
# check if drones on
# select one with battery 100%
# calculate distance and way


@receiver(m2m_changed, sender=Order.status_history)
def create_status_history(sender, instance, action, reverse, **kwargs):
    print(f'action : {action} | instance : {action}')



@receiver(post_save, sender=Order)
def handle_order_save(sender, instance, created, **kwargs):
    # post_save.disconnect(handle_post_save, sender=sender)

    def create_status():
        print("creating status history")
        # status = OrderStatus.objects.get(id=1)
        instance.status_history.set([instance.status])
        # print(f'status history {status}')

        # return instance

    def set_update():
        print("call set_update()")
        if instance.status.id == 1:
            print(f'order id :{instance.status.id} status: {instance.status.status} ')
            instance.status_id = 2
            instance.save()
            instance.status_history.add(instance.status)
            return instance

        # status = OrderStatus.objects.count()
        # print(f'status count: {status}')
        # status_cycle = cycle(status)
        # next_status = next(status_cycle)
        # for index in range(len(status) - 1):
        #     current_status, next_status = next_status, next(status_cycle)
        #     if instance.status.status == current_status:
        #         print(f'{index} status : {current_status} -> {next_status}')
        #         print(f'order id :{instance.status.id} status: {instance.status.status} ')
        #         instance.status_id = next_status
        #         instance.save()
        #         return instance

    if created:
        create_status()
        print(f'New record inserted: id: {instance.id} Status {instance.status} update_at {instance.updated_at}', )
    else:
        print(f'Record updated: id: {instance.id} Status {instance.status.status} update_at {instance.updated_at}', )
        # update_status_history()
        set_update()
        print(f'after update updated: id: {instance.id} Status {instance.status.status} update_at {instance.updated_at}', )
        # update_thread = threading.Thread(target=set_update, args=())
        # update_thread.run()

        # post_save.connect(handle_post_save, sender=sender)
        # post_save.disconnect(handle_post_save, sender=sender)
        # post_save.connect(handle_post_save, sender=sender)


@receiver(post_save, sender=OrderStatus)
def create_order_status(sender, instance, created, **kwargs):
    # post_save.disconnect(handle_post_save, sender=sender)
    def set_create():
        print("call set_update()")
        status = ["pending",
                  "in_aile",
                  "picking_from_aile",
                  "packaging_items",
                  "to_departure_door",
                  "in_departure_door",
                  "ready_to_fly",
                  "picking_by_drone",
                  "start_flying",
                  "in_air",
                  "landing",
                  "dropping_off",
                  "front_off_door",
                  "package_dropped_off",
                  "enjoy",
                  ]

        status_cycle = cycle(status)
        next_status = next(status_cycle)
        for index in range(len(status)-1):
            current_status, next_status = next_status, next(status_cycle)
            if instance.status == current_status:
                print(f'{index} status : {current_status} -> {next_status}')
                # instance.status = next_status
                OrderStatus.objects.create(status=next_status)
                # instance.save()
                # return instance

    if created:
        print(f'New record inserted: id: {instance.id} Status {instance.status} update {instance.updated_at}',)
        set_create()
    else:
        print(f'Record updated: id: {instance.id} Status {instance.status} update {instance.updated_at}', )
        # set_update()
        # update_thread = threading.Thread(target=set_update, args=())
        # update_thread.run()




@receiver(post_save, sender=Drone)
def handle_post_save(sender, instance, created, **kwargs):
    if created:
        print("New record inserted:", instance.status)
    else:
        print("Record updated: Status", instance.status)


@receiver(post_delete, sender=Order)
def handle_post_delete(sender, instance, **kwargs):
    print("Record deleted:", instance)


@receiver(pre_delete, sender=Order)
def handle_pre_delete(sender, instance, **kwargs):
    print("About to delete record:", instance)
