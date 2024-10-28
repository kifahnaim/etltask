from django.urls import path
from .views import TransactionList,ClientTransactionSummaryList

urlpatterns = [
    path('transactions/<int:client_id>/', TransactionList.as_view(), name='transaction-list'),
    path('transaction_summary/<int:client_id>/', ClientTransactionSummaryList.as_view(), name='client_transaction_summary'),

]
