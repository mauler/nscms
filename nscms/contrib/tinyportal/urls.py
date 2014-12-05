# # -*- coding: utf-8 -*-

# from django.conf.urls import patterns, url
# from django.conf import settings

# from opps.core.cache import cache_page

# from .views import ContainerList, ContainerDetail


# urlpatterns = patterns(
#     '',

#     url(r'^$', ContainerList.as_view(), name='home'),

#     url(r'^(?P<channel__long_slug>[\w//-]+)/(?P<slug>[\w-]+)\.html$',
#         cache_page(settings.OPPS_CACHE_EXPIRE_DETAIL)(
#             ContainerDetail.as_view()), name='container_open'),

#     url(r'^(?P<channel__long_slug>[\w\b//-]+)/$',
#         cache_page(settings.OPPS_CACHE_EXPIRE_LIST)(
#             ContainerList.as_view()), name='channel_open'),

# )
