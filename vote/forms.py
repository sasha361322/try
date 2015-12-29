from django.forms import *
from .models import *

class AnswerForm(ModelForm):
    class Mets:
        model = VoteDescription