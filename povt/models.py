from django.db import models

class Order(models.Model):
    order_text = models.CharField(max_length=200)
