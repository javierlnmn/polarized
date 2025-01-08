from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Subject, Vote


class VoteInline(admin.TabularInline):
    model = Vote
    extra = 1


@admin.register(Subject)
class SubjectAdmin(TranslationAdmin):
    list_display = ('name', 'description', 'result', 'total_votes')
    search_fields = ('name', 'description')

    fieldsets = (
        ('Subject Details', {
            'fields': (
                'name',
                'description',
            )
        }),
    )

    inlines = [VoteInline]

    def total_votes(self, obj):
        return obj.votes.count()
    total_votes.short_description = 'Total Votes'

    def result(self, obj):
        result_str = obj.result['result']
        return result_str.capitalize() if result_str else 'No data yet'
    result.short_description = 'Result'


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ('user', 'subject', 'value', 'created_at')
    readonly_fields = ('created_at',)
    list_filter = ('value', 'subject')
    search_fields = ('user__username', 'subject__name')

