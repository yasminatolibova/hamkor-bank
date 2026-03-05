from .views import TransferCreateView, TransferListView, TransactionList
from django.urls import path

urlpatterns=[
    path('transfer/', TransferCreateView.as_view(), name='transfer'),
    path('transferlist/', TransferListView.as_view(), name='transferlist'),
    path('transactionlist/', TransactionList.as_view(), name='transactionlist')
    
]