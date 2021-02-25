from django.db import models

# Create your models here.

class new_p(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    sq = models.IntegerField(default=0)
    price =  models.IntegerField(default=0)
    bath =  models.IntegerField(default=0)
    bed = models.IntegerField(default=0)
    address = models.TextField()
    sale = models.BooleanField(default=False)

class slides(models.Model):
    img = models.ImageField(upload_to='pics')
    status = models.CharField(max_length=20)
    desc = models.TextField()
    sq = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    bath = models.IntegerField(default=0)
    bed = models.IntegerField(default=0)
    rent = models.BooleanField(default=False)
    sale = models.BooleanField(default=False)


