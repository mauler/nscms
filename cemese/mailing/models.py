#!/usr/bin/env python
#-*- coding:utf-8 -*-

from django.contrib import admin
from django.conf import settings
from django.core.mail import EmailMessage, send_mail
from django.db import models
from django.template.loader import render_to_string



class MailModel(models.Model):
    template_name = getattr(settings, "CEMESE_MAILING_TEMPLATE_NAME", "cemese/mail_template.txt")
    mail_subject = getattr(settings, "CEMESE_MAILING_MAIL_SUBJECT", "Cemese mail")
    from_mail = getattr(settings, "CEMESE_MAILING_FROM_MAIL", "contato@construtoracarrara.com.br")
    to_mail = getattr(settings, "CEMESE_MAILING_TO_MAIL", ["proberto.macedo@gmail.com"])
    fail_silently = getattr(settings, "CEMESE_MAILING_FAIL_SILENTLY", True)

    mail_sent = models.BooleanField(verbose_name=u"Email enviado",
                                    default=False,
                                    editable=True)

    class Admin(admin.ModelAdmin):
        readonly_fields = ("mail_sent", )

    class Meta:
        abstract = True

    def send_email(self):
        if not self.mail_sent:
            if hasattr(self, "mailing"):
                for subject, template_name, getto in self.mailing:
                    html_content = render_to_string(template_name, {'instance': self})

                    if callable(subject):
                        subject = subject(self)

                    if callable(getto):
                        to = getto(self)
                    else:
                        to = self.to_mail

                    msg = EmailMessage(subject, html_content, self.from_mail, to)
                    if template_name.endswith(".html"):
                        msg.content_subtype = "html"
                    msg.send()
            else:
                message = render_to_string(self.template_name, {'instance': self})
                send_mail(self.mail_subject,
                          message,
                          self.from_mail,
                          self.to_mail,
                          fail_silently=self.fail_silently)
            self.mail_sent = True
            self.save()
            return True
        else:
            return False

    @staticmethod
    def post_save(sender, instance, created, *args, **kwargs):
        if created:
            instance.send_email()

