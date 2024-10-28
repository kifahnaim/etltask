from rest_framework import serializers
from .models import transactions,ClientTransactionSummary

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = transactions
        fields = '__all__'

class ClientTransactionSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientTransactionSummary
        fields = '__all__'         
