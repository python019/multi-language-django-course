from modeltranslation.translator import register, TranslationOptions
from .models import Malumot

@register(Malumot)
class MalumotTranslationOptions(TranslationOptions):
    fields = ('nomi', 'text',)