from django.contrib import admin
from .models import Choice,User,Vote,VoteDescription,VoteInformation

admin.site.register(Choice)
admin.site.register(User)
admin.site.register(Vote)
admin.site.register(VoteDescription)
admin.site.register(VoteInformation)