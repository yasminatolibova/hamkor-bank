from .views import QrcodeListCreate, QrcodeRetrieveDestroy
from django.urls import path
urlpatterns=[
    path('qrcode_createlist/', QrcodeListCreate.as_view(), name='qrcode_createlist'),
    path('qrcode_destroy/<int:pk>/', QrcodeRetrieveDestroy.as_view(), name='qrcode_destroy'),

]