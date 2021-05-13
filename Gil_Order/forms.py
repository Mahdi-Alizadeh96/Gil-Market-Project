from django import forms


class UserNewOrderForm(forms.Form):
    productId = forms.IntegerField(
        widget=forms.HiddenInput(),
    )
