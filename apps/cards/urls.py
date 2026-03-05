from .views import CardCreateView, CardListView
from django.urls import path

urlpatterns=[
    path('card/', CardCreateView.as_view(), name='card'),
    path('cardlist/', CardListView.as_view(), name='cardlist')
] 