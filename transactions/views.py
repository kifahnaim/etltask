from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from .serializers import TransactionSerializer,ClientTransactionSummarySerializer
from rest_framework.response import Response
from rest_framework import status,generics
from django.shortcuts import render
from .models import transactions,ClientTransactionSummary
# Create your views here.
        
class TransactionList(generics.ListAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated] 
    def get_queryset(self):
        client_id = self.kwargs['client_id']
        date = self.request.query_params.get('date', None)
        queryset = transactions.objects.filter(client_id=client_id)
        if date:
            try:
                parsed_date = timezone.datetime.strptime(date, '%Y-%m-%d').date()
                queryset = queryset.filter(transaction_date__date=parsed_date)
            except ValueError:
                pass  
        return queryset

class ClientTransactionSummaryList(generics.ListAPIView):
    serializer_class = ClientTransactionSummarySerializer

    def get_queryset(self):
        client_id = self.kwargs['client_id']
        queryset = ClientTransactionSummary.objects.all()  # Start with all objects
        print(client_id)
        if client_id is not None:
            queryset = queryset.filter(client_id=client_id)  # Filter by client_id if provided
        
        return queryset
