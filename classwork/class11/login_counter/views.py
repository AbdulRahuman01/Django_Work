from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Visit


def home(request):
    return render(request, 'login_counter/home.html')


def signup_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
        else:
            User.objects.create_user(username=username, password=password)
            messages.success(request, "Account created! Please login.")
            return redirect('login')

    return render(request, 'login_counter/signup.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('counter')
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'login_counter/login.html')


def logout_view(request):
    logout(request)
    return redirect('home')


from django.contrib import messages

def counter_view(request):
    if not request.user.is_authenticated:
        messages.warning(request, "Please login to see the count")
        return redirect('login')  # redirect to login page

    # Get or create visit record
    visit, created = Visit.objects.get_or_create(user=request.user)
    visit.count += 1
    visit.save()

    return render(request, 'login_counter/counter.html', {'count': visit.count})
