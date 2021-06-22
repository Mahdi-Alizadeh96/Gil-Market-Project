from django import forms


class CommentForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'نام خود را وارد کنید.', 'class': 'form-control mb-2 input-border'}),
    )

    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'placeholder': 'نظر خود را بنویسید...', 'class': 'form-control mb-2 input-border'}),
    )
