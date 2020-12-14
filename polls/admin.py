from django.contrib import admin
from .models import Question, Choice

# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice 
    extra = 4

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    fieldsets = (
        ('Question Content', { 'fields' : ['question_text']}),
        ('Date information', {'fields': ['pub_date']})
        )
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['question_text']



admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
