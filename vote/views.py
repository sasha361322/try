from django.shortcuts import render
from django.shortcuts import render_to_response
from models import VoteDescription

def view1(request):
    vote_descriptions = VoteDescription.objects.all()
    return render_to_response('vote/view1.html',{'vote_descriptions':vote_descriptions})