from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from .forms import NewUserForm
from shop.models import Order
from django.http import JsonResponse

def signup(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            messages.info(request, "Signed up successfully!")
            return redirect("/")

        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

            return render(request, "login/signup.html", context={"form":form})

    form = NewUserForm
    return render(request, "login/signup.html", context={"form":form})


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("/")


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, "login/login.html", context={"form":form})

def account(request):
    orders = Order.objects.all().order_by('-order_id')
    return render(request, 'login/account.html', {'orders' : orders})
