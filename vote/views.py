from django.shortcuts import render
from django.shortcuts import *
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import *
from forms import *
from django.core.context_processors import *

def votes(request):
    vote_descriptions = VoteDescription.objects.all()
    votes = Vote.objects.all()
    return render_to_response('vote/votes.html', {'vote_descriptions':vote_descriptions, 'votes':votes})


def vote(request, vote_id):
    vote = Vote.objects.get(id=vote_id)
    vote_description = VoteDescription.objects.filter(id_vote=vote_id)
    return render_to_response('vote/vote.html', {'vote':vote,'vote_description':vote_description})
"""
def vote(request, vote_id=1):
    answer_form=AnswerForm
    args={}
    args.update(csrf(request))
    args['vote']=Vote.objects.get(id=vote_id)
    args['answers']=VoteDescription.objects.filter(id_vote=vote_id)
    args['form']=answer_form
    return render_to_response('vote.html', args)
    """

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



