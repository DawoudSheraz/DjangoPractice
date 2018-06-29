# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.shortcuts import render, get_object_or_404
from .models import Questions, Choice


class IndexView(generic.ListView):

    template_name = "polls/add.html"
    context_object_name = 'latest'

    def get_queryset(self):
        return Questions.objects.order_by("-publish_date")[:5]


class DetailsView(generic.DetailView):
    model = Questions
    template_name = "polls/details.html"


class ResultsView(generic.DetailView):
    model = Questions
    template_name = "polls/results.html"


def voting(request, question_id):
    user_question = get_object_or_404(Questions, pk=question_id)
    try:
        selected_choice = user_question.choice_set.get(pk=request.POST['choice'])   # ID/PK of the selected choice
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/details.html", {"question": user_question})

    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question_id,)))

