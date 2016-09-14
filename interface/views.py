from django.http import HttpResponse
from django.template import loader
from .models import Account
# Create your views here.

def index(request):
    all_accounts = Account.objects.all()
    template = loader.get_template('interface/index.html')
    context = {
        'all_accounts': all_accounts,
    }
    return HttpResponse(template.render(context, request))

def show(request, account_id):
    return HttpResponse("<h2>Details for Account ID: " + str(account_id) + "</h2>")
