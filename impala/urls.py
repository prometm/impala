from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^specifications', views.specifications,name='specifications'),
    url(r'^gallery', views.gallery,name='gallery'),
    url(r'^about', views.about,name='about'),
    url(r'^store', views.store,name='store'),
]