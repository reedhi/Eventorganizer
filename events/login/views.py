from django.http import HttpResponse
from login.models import User
from django.template import loader
from django.shortcuts import render
from login.models import Event
from django.db import models
from django.core.mail import EmailMessage
from django.core.mail import send_mail


def index(request):
    return render(request,'login/loggedin.html')

def eventDetails(request):
    if request.method == "POST":
        print("*************************************************************************")
        print(request)
        username = request.POST['email']
        password = request.POST['pwd']

    userDetails = User.objects.filter(email = username)

    user = None
    for temp in userDetails:
        user = temp
        break

    if user != None:
        send_mail(
            'Log in from windows device',
            'You logged in from laptop',
            'yjani204@gmail.com',
            [user.email],
            fail_silently=False,
        )

    return render(request,'login/index.html',{"userDetails" : user })

def getEvent(request, userId):
    user = User.objects.filter(id = userId);
    print(user)
    temps = loader.get_template('login/index.html', using=None)
    context = {'user': user}
    return HttpResponse(temps.render(context, request))

def signUp(request):
    if request.method == "post":
       print("Its cae hear")
    return  HttpResponse("<h1>Congratulations<h1>")



