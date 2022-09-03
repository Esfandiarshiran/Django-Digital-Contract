from django.urls import path
from .views import success_contract, open_contract, confirm_contract
urlpatterns = [

    path('open-contract/', open_contract, name='open-contract'),
    path('confirm-contract/', confirm_contract, name='confirm-contract'),
    path('success-contract/', success_contract, name='success-contract'),

]
