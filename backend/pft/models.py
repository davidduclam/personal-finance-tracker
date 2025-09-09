from django.db import models

class Income(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField()

    def __str__(self):
        return self.name + ' $' + str(self.amount)
    
class Expense(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField()

    def __str__(self):
        return self.name + ' $' + str(self.amount)