

template_name
subject
from
to


    @staticmethod
    def post_save(sender, instance, created, *args, **kwargs):
        if created:
            message = render_to_string("coleguium/trabalhe_conosco_email.html",
                                       {'trabalheconosco': instance})
            send_mail(u"[COLEGUIUM] Fale Conosco",
                      message,
                      settings.TRABALHE_CONOSCO_FROM_EMAIL,
                      [settings.TRABALHE_CONOSCO_TO_EMAIL],
                      fail_silently=True)
            instance.enviado = True
            instance.save()

from django.db.models.signals import post_save

#post_save.connect(FaleConosco.post_save, sender=TrabalheConosco)

