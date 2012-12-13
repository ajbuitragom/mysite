<<<<<<< HEAD
from polls.models import Poll, Choice
from django.contrib import admin

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_filter = ['pub_date']


admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)
=======
#Se importa la base de datos con la tabla Poll
from polls.models import Poll
from django.contrib import admin

class PollAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question']

admin.site.register(Poll, PollAdmin)
>>>>>>> 9a96e522faf89ff297e67db776b5c70f05749063
