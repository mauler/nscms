#-*- coding:utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from nscms.db.models import ContentModel, SimpleContentModel


class Question(ContentModel):
    finished = models.BooleanField(
        verbose_name=u"Finalizada",
        help_text=u"Indica que a enquete esta finalizada.",
        default=False)

    class Meta:
        verbose_name = _(u"Pergunta")
        verbose_name_plural = _(u"Perguntas")

    def get_choices(self):
        qs = self.choice_set.order_by('-votes')
        votes = .0
        for i in qs:
            votes += i.votes
        return [{'object': i,
                 'percent': ("%.1f" % (i.votes / votes * 100)).zfill(4)} \
                for i in self.choice_set.order_by('-votes')]


class Choice(SimpleContentModel):
    question = models.ForeignKey(Question)
    votes = models.IntegerField(default=0)

    class Meta:
        verbose_name = _(u"Resposta")
        verbose_name_plural = _(u"Respostas")

    def __str__(self):
        return '%s - %s' % (self.question.title, self.title)
