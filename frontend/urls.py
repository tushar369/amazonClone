from django.urls import path
from .views import main

urlpatterns = [

    path('', main, name='reactHtmlpage'),
    path('accounts/', main, name='accounts-page')
]