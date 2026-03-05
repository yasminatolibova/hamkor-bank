from django.db import models
from dateutil.relativedelta import relativedelta
from django.utils import timezone

# Create your models here.

from ..accounts.models import User

class Card(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='card+')
    card_number=models.CharField(max_length=16)
    balance=models.DecimalField(max_digits=20, decimal_places=2, default=0)
    is_blocked=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now=True)

    def expire_date(self):
        return timezone.now() > self.created_at +relativedelta(years=5)
    
    def __str__(self):
        return f"{self.card_number}"


