from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.add_preferences, name='add_preferences'),
    path('news_list', views.news_list, name='news_list'),
    path('news_check', views.news_keywords, name='news_check')
]

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()