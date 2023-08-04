from django.db import models


# class Status(models.Model):
#     code = models.CharField(max_length=200, unique=True)
#     brief = models.CharField(max_length=550, unique=True)
#     description = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)


class History(models.Model):
    command = models.CharField(max_length=550, unique=True)
    brief = models.CharField(max_length=550)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # status = models.OneToOneField(Status, on_delete=models.CASCADE)
