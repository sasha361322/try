from django.shortcuts import render
from django.shortcuts import render_to_response
from .models import *

def votes(request):
    vote_descriptions = VoteDescription.objects.all()
    themes = Vote.objects.all()
    return render_to_response('vote/votes.html', {'vote_descriptions':vote_descriptions, 'themes':themes})


def vote(request, vote_id):
    return render_to_response('vote/vote.html', {'vote':Vote.objects.get(id_description=vote_id),'vote_description':VoteDescription.objects.filter(id_desc=vote_id)})