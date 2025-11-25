from modeltranslation.translator import TranslationOptions, translator

from .models import Subject


class SubjectTranslationOptions(TranslationOptions):
    fields = ("name", "description")


translator.register(Subject, SubjectTranslationOptions)
