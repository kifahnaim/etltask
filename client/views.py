from django.shortcuts import render
from .models import clients
from transactions.views import transactions
# Create your views here.
def get_client(id):
    clients.objects.get(client_id=id)
    
def get_client_transactions(id):
    transactions.objects.get(client=id)