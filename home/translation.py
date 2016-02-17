from models import *
from modeltranslation.translator import register, TranslationOptions

# TODO: Find good solution for default value dublication


@register(FacultyMember)
class FacultyMemberTranslationOptions(TranslationOptions):
    fields = ('interest', 'bio')
    required_languages = ('en', 'tr')


@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ('title', 'abstract')
    required_languages = ('en', 'tr')


@register(NewsEvent)
class NewsEventTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
    required_languages = ('en', 'tr')


@register(Program)
class ProgramTranslationOptions(TranslationOptions):
    fields = ('title',)
    required_languages = ('en', 'tr')


@register(ProgramSubField)
class ProgramSubFieldTranslationOptions(TranslationOptions):
    fields = ('title', 'text')
    required_languages = ('en', 'tr')


@register(OtherText)
class OtherTextTranslationOptions(TranslationOptions):
    fields = ('text',)
    required_languages = ('en', 'tr')
