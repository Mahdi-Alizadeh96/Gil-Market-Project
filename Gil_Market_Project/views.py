from django.shortcuts import render


# header code behind
def header(request, *args, **kwargs):
    context = {}
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
