from djongo import models
from pymongo import MongoClient
from django.conf import settings
from statistics import mean

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    img_url = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    mod_date = models.DateTimeField(auto_now_add=True)
    serial_num = models.IntegerField()
    price = models.DecimalField(max_digits=20, decimal_places=2)
    # rating = models.DecimalField(max_digits=3, decimal_places=1)
    
    def __str__(self):
        return self.name

    def get_comments(self):
        comms = Comment.objects.filter(prod_num=self.serial_num).order_by('-pub_date')[:5]
        com_arr = []
        for com in comms:
            com_user = Usuario.objects.get(email=com.user_mail).nickname
            com_arr.append([com_user, com])
        return com_arr
    
    def get_all_comments(self):
        comms = Comment.objects.filter(prod_num=self.serial_num).order_by('-pub_date')
        return comms
    
    # def update_rating(self):
    #     coll_prod = client['catalogo_product']
    #     # db_comm = client['catalogo_comment']
    #     comms = Comment.objects.filter(prod_num=self.serial_num)
    #     rates = []
    #     for comm in comms:
    #         rates.append(comm.prod_rating)
            
    #     coll_prod.update_one({'serial_num':self.serial_num}, {'$set':{'rating': round(mean(rates), 1)}})
    
    def call_rating(self):
        comms = Comment.objects.filter(prod_num=self.serial_num)
        rates = []
        for comm in comms:
            rates.append(float(str(comm.prod_rating)))
        if len(rates) > 0:
            return round(mean(rates), 1)
        else:
            return 0.0
class Comment(models.Model):
    prod_rating = models.DecimalField(max_digits=3, decimal_places=1)
    prod_num = models.IntegerField()
    pub_date = models.DateTimeField(auto_now_add=True)
    user_mail = models.EmailField()
    text_comment = models.TextField()
    
    def __str__(self):
        return self.text_comment
class Usuario(models.Model):
    email = models.EmailField(primary_key=True, max_length=40)
    nickname = models.CharField(max_length=100)
    realname = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nickname