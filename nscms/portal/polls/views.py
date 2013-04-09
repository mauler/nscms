#!/usr/bin/env python
#-*- coding:utf-8 -*-

from feincms.views.generic.list_detail import object_detail

from models import Choice


def vote(request, choice_id=None,
    template="nscsm/portal/polls/question_result.html"):

    choice = Choice.objects.get(pk=choice_id or
                                request.POST.get('choice_id') or
                                request.GET.get('choice_id'))
    choice.votes += 1
    choice.save()
    qs = choice.question.choice_set.order_by('-votes')
    votes = .0
    for i in qs:
        votes += i.votes
    return object_detail(request=request,
                         queryset=Choice.objects.all(),
                         object_id=choice.id,
                         template_name=template,
                         extra_context={
                            "choices":
                             [{'object': i, 'percent': ("%.1f" % (i.votes / votes * 100)).zfill(4)} for i in choice.question.choice_set.order_by('-votes')]#Choice.objects.filter(question=)
                         })
