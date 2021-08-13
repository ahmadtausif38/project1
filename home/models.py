from django.db import models
from autoslug import AutoSlugField
from tinymce.models import HTMLField

CATEGORY_CHOICES=(
    ('Mob','Mobile'),
    ('Lap','Laptop'),
    ('Cam','Camera'),
    ('Ear','Earphone'),
)
BRAND_CHOICES=(
    ('Apple','Apple'),
    ('Samsung','Samsung'),
    ('Sony','Sony'),
    ('Mi','Mi'),
    ('Realme','Realme'),
)
# Create your models here.
class product(models.Model):
    pro_name=models.CharField(max_length=100)
    pro_brand=models.CharField(choices=BRAND_CHOICES,max_length=10)
    pro_img=models.ImageField(upload_to='Images')
    pro_price=models.IntegerField()
    pro_category=models.CharField(choices=CATEGORY_CHOICES,max_length=5)
    pro_desc=HTMLField()
    #pro_slug=AutoSlugField(populate_from='pro_name',unique=True,null=True,default=None)


class contacts(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    message=models.TextField(max_length=200)