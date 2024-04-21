
from django.urls import path
from app.views import *

urlpatterns = [
    # this is index page
    path('', Index),

    # this is auth pages
    path('login/', Login),
    path('register/', Register),
]
