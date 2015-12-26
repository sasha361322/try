from __future__ import unicode_literals
from django.db import models
from django.shortcuts import render_to_response

class Choice(models.Model):
    id = models.IntegerField(primary_key=True)
    number_1 = models.IntegerField(db_column='1')  # Field renamed because it wasn't a valid Python identifier.
    number_2 = models.IntegerField(db_column='2')  # Field renamed because it wasn't a valid Python identifier.
    number_3 = models.IntegerField(db_column='3', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_4 = models.IntegerField(db_column='4', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_5 = models.IntegerField(db_column='5', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_6 = models.IntegerField(db_column='6', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_7 = models.IntegerField(db_column='7', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_8 = models.IntegerField(db_column='8', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_9 = models.IntegerField(db_column='9', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_10 = models.IntegerField(db_column='10', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'choice'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'user'


class Vote(models.Model):
    id = models.IntegerField(primary_key=True)
    theme = models.CharField(max_length=100)
    date = models.DateTimeField()
    count = models.IntegerField()
    is_single = models.IntegerField()
    id_description = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'vote'

def __str__(self):
    return self.theme

class VoteDescription(models.Model):
    id = models.IntegerField(primary_key=True)
    answer1 = models.CharField(max_length=100)
    answer2 = models.CharField(max_length=100)
    answer3 = models.CharField(max_length=100, blank=True, null=True)
    answer4 = models.CharField(max_length=100, blank=True, null=True)
    answer5 = models.CharField(max_length=100, blank=True, null=True)
    answer6 = models.CharField(max_length=100, blank=True, null=True)
    answer7 = models.CharField(max_length=100, blank=True, null=True)
    answer8 = models.CharField(max_length=100, blank=True, null=True)
    answer9 = models.CharField(max_length=100, blank=True, null=True)
    answer10 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vote_description'

#def view_vote_descriptions(request):
#	vote_descriptions = VoteDescription.objects.all()
        #return render_to_response('try/vote/templates/vote/view1.html',{'vote_descriptions':vote_descriptions})
 #       return render_to_response('vote/view1.html',{'vote_descriptions':vote_descriptions})


class VoteInformation(models.Model):
    id = models.IntegerField(primary_key=True)
    id_user = models.ForeignKey(User, models.DO_NOTHING, db_column='id_user', blank=True, null=True)
    id_vote = models.IntegerField()
    date = models.DateTimeField()
    id_choice = models.IntegerField()
    ip = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'vote_information'
