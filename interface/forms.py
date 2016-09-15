from django import forms

TRANSACTION_TYPES= (
    ('1', 'Deposit'),
    ('2', 'Withdrawal'),
    ('3', 'Transfer'),
)

class AccountForm(forms.Form):
    name = forms.CharField(max_length=75)
    address = forms.CharField(max_length=200)
    phone_number = forms.CharField(max_length=12)
    balance = forms.DecimalField(max_digits=12, decimal_places=2, default=0.00)

class TransactionForm(forms.Form):
    name = forms.CharField(label='Description', max_length=25)
    transaction_type = forms.CharField(label='Type', max_length=10)
    amount = forms.DecimalField(max_digits=12, decimal_places=2)
    account_to = forms.ChoiceField(choices=TRANSACTION_TYPES)
