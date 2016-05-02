from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^footer-email/$', views.footer_email, name='footer_email'),
]
