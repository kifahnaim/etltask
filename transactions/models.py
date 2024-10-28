from django.db import models
from client.models import *
# Create your models here.
    
class transactions(models.Model):
    transaction_id = models.IntegerField( primary_key=True)
    client = models.ForeignKey(clients, on_delete=models.CASCADE, related_name='transactions')
    transaction_type = models.CharField(max_length=50)
    transaction_date = models.DateTimeField()
    amount= models.DecimalField(max_digits=10, decimal_places=2)
    currency=models.CharField( max_length=50)
    class Meta:
        db_table = "transactions"  



class ClientTransactionSummary(models.Model):
    client_id = models.IntegerField( primary_key=True)
    name = models.CharField()
    total_transactions = models.IntegerField()
    total_spent = models.DecimalField(max_digits=10, decimal_places=2)
    total_gained = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False 
        db_table = 'client_transaction_summary'  # The name of the materialized view

