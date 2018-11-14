from django.db import models

# Create your models here.

# python manage.py makemigration - this will create the migrations file
# python manage.py migrate = this will actually create the DB table


class TrackingShipment(models.Model):
    transaction = models.CharField(max_length=30)
    poNumber = models.CharField(max_length=30)
    deliveryLoc = models.TextField()
    shipVia = models.CharField(max_length=10)
    tId = models.IntegerField()  # tessco ID
    description = models.TextField()
    container = models.CharField(max_length=30)
    carrier = models.CharField(max_length=30)
    trackingNo = models.CharField(max_length=30)
    qtyShipped = models.IntegerField()
    shipInvoiceDate = models.DateTimeField()


def __str__(self):
    return self.poNumber
