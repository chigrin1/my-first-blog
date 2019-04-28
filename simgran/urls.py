from django.shortcuts import url
from . import views

urlpatterns = [
    path('$', view.index, simgran),
]
