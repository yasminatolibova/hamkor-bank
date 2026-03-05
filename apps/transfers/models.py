from django.db import models
from ..accounts.models import Accounts

# Create your models here.

class Transfer(models.Model):
    from_account=models.ForeignKey(Accounts, on_delete=models.CASCADE, related_name='outgoing transaction+')
    to_account=models.ForeignKey(Accounts, on_delete=models.CASCADE, related_name='ingoing transaction+')
    amount=models.DecimalField(max_digits=10, decimal_places=2)
    STATUS=[
        ('pending', 'Pending'),
        ('success', 'Success'),
        ('failed', 'Failed')
    ]
    
    status=models.CharField(max_length=50, choices=STATUS, default='pending')
    created_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.amount}"
    
class Transaction(models.Model):
    account=models.ForeignKey(Accounts, on_delete=models.CASCADE, related_name='transaction history+')
    amount=models.DecimalField(max_digits=15, decimal_places=2)
    TYPE=[
        ('credit', 'Credit'),
        ('debit', 'Debit')
    ]
    type=models.CharField(max_length=20, choices=TYPE)
    description=models.CharField(max_length=250)
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-created_at']

    def __str__(self):
        return f"{self.account}"


    


    