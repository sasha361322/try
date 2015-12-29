from django.shortcuts import render
from django.shortcuts import *
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import *
from forms import *
from django.core.context_processors import *
from datetime import datetime
"""
def votes(request):
    vote_descriptions = VoteDescription.objects.all()
    votes = Vote.objects.all()
    return render_to_response('vote/votes.html', {'vote_descriptions':vote_descriptions, 'votes':votes})
"""
def votes(request):
    vote_form = VoteForm
    args = {}
    args.update(csrf(request))
    args['vote_descriptions'] = VoteDescription.objects.all()
    args['votes'] = Vote.objects.all()
    args['form'] = vote_form
    return render_to_response('vote/votes.html', args)

def vote(request, vote_id):
    vote = Vote.objects.get(id=vote_id)
    vote_description = VoteDescription.objects.filter(id_vote=vote_id)
    return render_to_response('vote/vote.html', {'vote':vote,'vote_description':vote_description})

def addanswer(request, description_id):
    try:
        if description_id in request.COOKIES:
            redirect('/')
        else:
            description = VoteDescription.objects.get(id=description_id)
            description.count += 1
            description.save()
            response = redirect('/')
            response.set_cookie(description_id, "test")
            return response
    except ObjectDoesNotExist:
        raise Http404
    return redirect ("/")


def addvote(request):
    if request.POST:
        form = VoteForm(request.POST)
        if form.is_valid():
            vote = form.save(commit=False)
            vote.date = datetime.now()
            vote.is_single = 1
            form.save()
    return render_to_response('vote/addanswers.html', args)

def addanswers(request, vote_id, n):
    if request.POST:
        form = AnswerForm(request.POST)
        if form.is_valid():
            votedescription = form.save(commit=False)
            votedescription.count = 0
            votedescription.number = n
            votedescription.id_vote = vote_id
            form.save()
            vote = Vote.objects.get(id=vote_id)
    return render_to_response('vote/addanswers.html', args)








"""
def vote(request, vote_id=1):
    answer_form=AnswerForm
    args={}
    args.update(csrf(request))
    args['vote']=Vote.objects.get(id=vote_id)
    args['answers']=VoteDescription.objects.filter(id_vote=vote_id)
    args['form']=answer_form
    return render_to_response('vote.html', args)

def addanswer(request, vote_id, vote_description_id_descs):
    try:
        vote = Vote.objects.get(id=vote_id)
        for v in vote_description_id_descs:
            desription = VoteDescription.objects.get(id=vote.id_description, number=v)
            desription.count += 1
            desription.save()
    except ObjectDoesNotExist:
        raise Http404
    return redirect ("/")
    """



