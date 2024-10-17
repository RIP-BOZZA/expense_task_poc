from django.db import models
from django.contrib.auth.models import User


class UserDetails(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    monthly_salary = models.DecimalField(max_digits=10,decimal_places=4)

    def __str__(self):
        return self.user.username


class Expense(models.Model):
    user = models.ForeignKey(User ,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10 ,decimal_places=4)
    category = models.CharField(max_length=50)
    year = models.CharField(max_length=4)
    month = models.CharField(max_length=10)
    def __str__(self):
        return self.name