from django.shortcuts import render, get_object_or_404
from .models import Account
# Create your views here.

def index(request):
    all_accounts = Account.objects.all()
    return render(request, 'interface/index.html', {'all_accounts': all_accounts})

def show(request, account_id):
    account = get_object_or_404(Account, pk=account_id)
    return render(request, 'interface/show.html', {'account': account})
