from django.contrib import admin

# Register your models here.
from .models import Question


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('subject', 'content', 'create_date')
    list_filter = ['subject']
    search_fields = ['content']


admin.site.register(Question)
