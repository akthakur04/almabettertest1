from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('marks', marks, name='marks'),
    path('rank', rank, name='rank'),
    path('sortnsearch', sortnsearch, name='sortnsearch'),
]
