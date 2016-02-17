from django.contrib import admin
from home.models import *
from home.forms import *


@admin.register(FacultyMember)
class FacultyMemberAdmin(admin.ModelAdmin):
    form = FacultyMemberForm
    exclude = ('interest', 'bio')


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    form = PublicationForm


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    exclude = ('title', 'abstract')


@admin.register(ResearchGroup)
class ResearchGroupAdmin(admin.ModelAdmin):
    pass


@admin.register(NewsEvent)
class NewsEventAdmin(admin.ModelAdmin):
    exclude = ('title', 'description')


class ProgramSubFieldAdminLine(admin.TabularInline):
    model = ProgramSubField
    exclude = ('title', 'text')


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    exclude = ('title',)
    form = ProgramForm
    inlines = (ProgramSubFieldAdminLine,)


@admin.register(OtherText)
class OtherTextAdmin(admin.ModelAdmin):
    readonly_fields = ('title',)
    exclude = ('text',)

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(IndustrialRelations)
class IndustrialRelationsAdmin(admin.ModelAdmin):
    pass
