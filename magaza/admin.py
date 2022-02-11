from django import forms
from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Magaza)
admin.site.register(models.Post)