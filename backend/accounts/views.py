from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User


def register(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'USERNAME is taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'EMAIL is taken!')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email)
                user.save()
                messages.info(request, 'USER CREATED!')
                return redirect('register')

        else:
            messages.info(request, 'bad password, pass1 =!= pass2')
            return redirect('register')

    else:
        return render(request, 'register.html')