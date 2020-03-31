from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def register_email(email_to):
    send_mail(
        'HELLO ZIOMEK!',
        'od dzisiaj jestes w naszej bazie',
        settings.EMAIL_HOST_USER,
        [email_to]
    )


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

                register_email(email)
                messages.info(request, 'email was sanding')

                user.save()
                messages.info(request, 'USER CREATED!')
                return redirect('register')
        else:
            messages.info(request, 'bad password, pass1 =!= pass2')
            return redirect('register')
    else:
        return render(request, 'register/register.html')
