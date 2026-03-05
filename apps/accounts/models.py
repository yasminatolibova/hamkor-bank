from django.db import models


class ID_CARD(models.Model):
    full_name=models.CharField(max_length=250)
    date_of_birth=models.DateField()
    personal_number=models.CharField(max_length=14, unique=True)

    def __str__(self):
        return f"{self.full_name}"

class User(models.Model):
    username=models.CharField(max_length=250, unique=True)
    email=models.EmailField(max_length=50)
    full_name=models.CharField(max_length=250)
    passport=models.ForeignKey(ID_CARD, on_delete=models.CASCADE)
    phone=models.CharField(max_length=20, unique=True)
    address=models.CharField(max_length=250)
    created_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
    
    

class Accounts(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='account+')
    account_number=models.CharField(max_length=20, unique=True, blank=True, null=True)
    balance=models.DecimalField(max_digits=20, decimal_places=2, default=0)
    currency=models.CharField(max_length=5, default='USD')
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user}"
