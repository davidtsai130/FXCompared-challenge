from django.http import HttpResponse
from django.shortcuts import render
from .models import Account
# Create your views here.

def index(request):
    all_accounts = Account.objects.all()
    context = {'all_accounts': all_accounts}
    return render(request, 'interface/index.html', context)

def show(request, account_id):
    return HttpResponse("<h2>Details for Account ID: " + str(account_id) + "</h2>")
