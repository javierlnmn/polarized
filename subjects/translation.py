from modeltranslation.translator import translator, TranslationOptions
from .models import Subject


class SubjectTranslationOptions(TranslationOptions):
    fields = ('name', 'description')

translator.register(Subject, SubjectTranslationOptions)