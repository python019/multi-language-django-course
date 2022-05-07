from django.contrib import admin
from .models import Malumot
from modeltranslation.admin import TranslationAdmin
# Register your models here.

@admin.register(Malumot)
class MalumotAdmin(TranslationAdmin):
    prepopulated_fields = {'slug': ('nomi',)}