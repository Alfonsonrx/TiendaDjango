from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    pub_date = models.DateTimeField()
    mod_date = models.DateTimeField()
    serial_num = models.IntegerField()
    price = models.DecimalField(max_digits=20, decimal_places=2)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    
    def __str__(self):
        return self.name
    
class Comment(models.Model):
    prod_rating = models.DecimalField(max_digits=3, decimal_places=1)
    prod_num = models.IntegerField()
    pub_date = models.DateTimeField()
    user_id = models.IntegerField()
    text_comment = models.TextField()