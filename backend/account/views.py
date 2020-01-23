from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from backend.account.sendMail import sendMail


# Create your views here.
def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                print("username is taken!")
            elif User.objects.filter(email=email).exists():
                print("email is taken!")
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username,
                                                password=password1, email=email)
                user.save()
                sendMail(email)

                print("HURAY! we have new User!")

        else:
            print("bad password....")

        return redirect('/')

    else:
        return render(request, 'register.html')


