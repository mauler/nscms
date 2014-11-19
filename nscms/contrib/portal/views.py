from django.views.generic.list import ListView, DetailView

from .models import Container


class ContainerMixin(object):
    model = Container

    def get_queryset(self):
        return Container.objects.published()


class ContainerDetailView(ContainerMixin, DetailView):
    pass


class ContainerListView(ContainerMixin, ListView):
    pass
