from django.conf.urls import url
from . import views
urlpatterns = [
  url(r'^survey$', views.index),
  url(r'^result$', views.index)
]