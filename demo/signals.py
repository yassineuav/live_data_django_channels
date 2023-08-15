import asyncio
import threading
import time
from itertools import cycle

from django.db.models.signals import post_save, post_delete, pre_delete, m2m_changed
from django.dispatch import receiver

from demo.models import Order, Drone, OrderStatus, OrderHistory


# if the status pending
# check the weight if the wight < 50 and last update < 2 minutes
# else return notification to admin dashboard weight is to heavy
#
# check if drones on
# select one with battery 100%
# calculate distance and way


# @receiver(m2m_changed, sender=Order.)
# def create_status_history(sender, instance, action, reverse, **kwargs):
#     print(f'action : {action} | instance : {action}')


@receiver(post_save, sender=Order)
def handle_order_save(sender, instance, created, **kwargs):
    # post_save.disconnect(handle_post_save, sender=sender)

    def create_status():
        print("creating status history")
        # status = OrderStatus.objects.get(id=1)
        # status, _created = OrderHistory.objects.get_or_create(id=1)
        # status, _created = OrderHistory.objects.get_or_create(order_history_id=instance.id)
        # print(f'creating new status {status}  | else _created {_created}')
        # print(f'status {status} created {_created}')
        # instance.status = status.status
        # instance.status_history.set([status])
        # instance.save()
        # return instance

    def set_status_pending():
        if instance.status_id != 1:
            print("clearing status history")
            deleted_count, deleted_data = OrderHistory.objects.filter(order_history_id=instance.id).delete()
            print(f"Deleted {deleted_count} OrderHistory instances. ")
            status, _created = OrderHistory.objects.get_or_create(
                order_history_id=instance.id,
                status='pending',
                status_id=1,
            )
            print(f'creating new status {status}  | else _created {_created}')
            instance.status_id = 1
            instance.status = 'pending'
            instance.save()
            return instance

    def set_update():
        status = OrderStatus.objects.count()
        time.sleep(2)
        if instance.status_id != status:
            print("updating status & adding next status_history")
            for index in range(1, status):
                if instance.status_id == index:
                    # time.sleep(2)
                    next_status = index + 1
                    update_status = OrderStatus.objects.get(id=next_status)
                    instance.status = update_status.status
                    instance.status_id = update_status.id
                    my_status, _created = OrderHistory.objects.get_or_create(
                        status=update_status.status,
                        status_id=update_status.id,
                        order_history_id=instance.id
                    )
                    print(f'status {instance.status} -> next {update_status.status}')
                    # instance.status_history.add(my_status)
                    instance.save()
                    return instance

    if created:
        print(f'New record inserted: id: {instance.id} Status {instance.status} update_at {instance.updated_at}', )
        create_status()
    else:
        print(f'Record updated: id: {instance.id} Status {instance.status} update_at {instance.updated_at}', )
        if instance.trigger == 0:
            set_status_pending()
            # create_status()
        else:
            # set_update()
            update_thread = threading.Thread(target=set_update, args=())
            # update_thread.run()
            update_thread.start()

        # Connect the signal handler using Django's signal framework
        # my_signal.connect(signal_handler)

        # Create and start a separate thread for signal handling
        # signal_thread = threading.Thread(target=my_signal.send, args=(sender_instance,))
        # signal_thread.start()


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
        # set_create()
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

