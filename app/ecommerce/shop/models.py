from django.db import models

# Create your models here.
class Orders(models.Model):
    order_id = models.AutoField(auto_created=True, primary_key=True)
    order_date = models.DateField(auto_now=True)
    amount = models.FloatField()
    item_id = models.CharField(max_length=100)
    

    