from django.contrib import admin
from .models import *

## Register your models here.
model_list = [Natjecanje,Sudionik,Profesor]
admin.site.register(model_list)