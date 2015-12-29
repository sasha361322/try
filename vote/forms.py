from django.forms import *
from .models import Vote, VoteDescription

class VoteForm(ModelForm):
    class Meta:
        model = Vote
        fields = ['theme', 'count']

class AnswerForm(ModelForm):
    class Meta:
        model = VoteDescription
        fields = ['answer']