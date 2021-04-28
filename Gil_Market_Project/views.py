from django.shortcuts import render
from base_user_account.models import User


# header code behind
def header(request, *args, **kwargs):
    firstName = None
    if request.user.is_authenticated:
        firstName = request.user.first_name

    context = {
        'firstName': firstName
    }
    return render(request, 'shared/Header.html', context)


# footer code behind
def footer(request, *args, **kwargs):
    context = {}
    return render(request, 'shared/Footer.html', context)


# code behind
def home_page(request):
    context = {
        'data': 'new_data'
    }
    return render(request, 'home_page.html', context)
