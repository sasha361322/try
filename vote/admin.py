from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(VoteInformation)

class VoteDescriptionInLine(admin.StackedInline):
    model = VoteDescription
    extra = 2

class VoteDescriptionAdmin(admin.ModelAdmin):
    fields = ['answer']
    inlines = [VoteDescriptionInLine]
admin.site.register(VoteDescription, VoteDescriptionAdmin)

class VoteInLine(admin.StackedInline):
    model = Vote
    extra = 2

class VoteAdmin(admin.ModelAdmin):
    fields = ['theme']
    inlines = [VoteInLine]
    list_filter = ['date']
admin.site.register(Vote, VoteAdmin)