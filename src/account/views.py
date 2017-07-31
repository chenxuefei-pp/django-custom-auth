from django.core.mail import send_mail
from django.shortcuts import render



def login(request):
    return render(request,'account/login.html')