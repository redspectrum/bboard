from django.urls import path

from .views import index, by_rubric
from .views import BbCreateView

from .views import *

urlpatterns = [
    path('add/', add_and_save, name='add'),
    # path('add/', BbCreateView.as_view(), name='add'),
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('', index, name='index'),
    path('detail/<int:pk>/', BbDetailView.as_view(), name='detail'),
]
