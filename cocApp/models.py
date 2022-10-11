from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class CabBooking(models.Model):
    bookingid = models.CharField(max_length=30,default=1)
    ticketNo = models.CharField(max_length=30,primary_key=True,default="Review")
    journeyDate = models.CharField(max_length=30)
    routeValue = models.CharField(max_length=30)
    route = models.CharField(max_length=70)
    seatNo = models.CharField(max_length=10)
    name = models.CharField(max_length=70)
    mobileNo = models.CharField(max_length=10,null=True,blank=True)
    pickupTime = models.CharField(max_length=10)
    pickupValue = models.CharField(max_length=30)
    pickupLocation = models.CharField(max_length=70)
    droppingLocation = models.CharField(max_length=70,null=True,blank=True)
    droppingValue = models.CharField(max_length=30)
    luggage = models.CharField(max_length=100,null=True,blank=True)
    amount = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.bookingid + "-" +self.name + "-" + self.mobileNo
