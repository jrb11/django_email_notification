from email.message import EmailMessage
from django.conf import settings
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from User_Login import settings
from django.core.mail import send_mail


def signup(request):
    if request.method == "POST":
        #print("0")
        #retrive username and password from signin.html file
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        #print("1")

        #Wait for user is activate account or not
        myuser.is_active = False

        myuser.save()  
        #print("2")

        messages.success(request, "Your Account has been created succesfully!! Please check your email to confirm your email address in order to activate your account.")
        #print("3")
        
        #welcome to email
        subject = "Welcome to Developer.JRB...!"
        message = "Hello " + myuser.first_name + "!! \n" + "Welcome to Dev.JRB!! \nThank you for visiting our website\n. We have also sent you a confirmation email, please confirm your email address. \n\nThanking You\nJay Bhadeshiya"
        from_email = settings.EMAIL_HOST_USER
        to_list= [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True) 
        #print("4")
