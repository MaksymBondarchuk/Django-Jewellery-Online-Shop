from django import forms


class OrderForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(widget=forms.Textarea, required=True)
    phone = forms.CharField(max_length=20)
    address = forms.CharField(max_length=250)
