from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def demo(request):

    return render(request, "base.html")


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "invalid credentials")
            return redirect("credentials:login")
    return render(request, "user.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['passworda']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username taken")
                return redirect('credentials:register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                print("user registered")
                return redirect("credentials:login")

        else:
            print('password not matched')
            return redirect("credentials:register")
    return render(request, "register.html")


def logout(request):
    auth.logout(request)
    return redirect("/")
