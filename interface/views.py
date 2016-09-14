from django.http import Http404
from django.shortcuts import render
from .models import Account
# Create your views here.

def index(request):
    all_accounts = Account.objects.all()
    return render(request, 'interface/index.html', {'all_accounts': all_accounts})

def show(request, account_id):
    try:
        account = Account.objects.get(pk=account_id)
    except Account.DoesNotExist:
        raise Http404("Account does not exist")
    return render(request, 'interface/show.html', {'account': account})
