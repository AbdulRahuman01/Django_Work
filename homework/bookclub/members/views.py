from django.shortcuts import render,redirect
from .models import Visit

from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def home(request):
    # Get or create a Visit object for the current user
    visit, created = Visit.objects.get_or_create(user=request.user)
    visit.count += 1
    visit.save()

    return render(request, 'members/home.html', {'visit_count': visit.count})

from django.contrib.auth.models import User
from django.contrib import messages

def signup_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
        else:
            User.objects.create_user(username=username, password=password)
            messages.success(request, "Account created successfully. Please log in.")
            return redirect('login')

    return render(request, 'members/signup.html')

from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # log the user in
            request.session['visit_count'] = 0  # reset visit counter on new login
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'members/login.html')


from django.contrib.auth import logout

def logout_view(request):
    logout(request)  # ends the user session
    return redirect('login')
