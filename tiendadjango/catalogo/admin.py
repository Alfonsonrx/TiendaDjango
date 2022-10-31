from django.contrib import admin
from .models import Product, Comment, Usuario

# Register your models here.
admin.site.register([Product, Comment, Usuario])