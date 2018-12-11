from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def home(request):

    return render(request, 'artisanstuple/home.html')

#def client_register(request):
    # return render(request, 'artisanstuple/client-register.html')

def customer_register(request):
     return render(request, 'artisanstuple/customer-register.html')

def login(request):
     return render(request, 'artisanstuple/login.html')
def register(request):
     return render(request, 'artisanstuple/register.html')


