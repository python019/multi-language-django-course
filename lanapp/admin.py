from django.contrib import admin
from .models import Malumot
# Register your models here.

@admin.register(Malumot)
class MalumotAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nomi',)}