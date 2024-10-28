from django.db import models


class clients(models.Model):
    client_id = models.IntegerField( primary_key=True)
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=50,unique=True)
    date_of_birth = models.DateField()
    country= models.CharField(max_length=150)
    account_balance=models.DecimalField(max_digits=10, decimal_places=2)
    class Meta:
        db_table = "clients"  
        constraints = [
            models.UniqueConstraint(fields=['email'], name='unique_email_constraint')  # Explicit unique constraint
        ]
    