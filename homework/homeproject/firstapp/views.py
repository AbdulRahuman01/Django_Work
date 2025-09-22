from django.shortcuts import render,redirect
from .forms import SignUpForm

def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.first_name = form.cleaned_data['name']  # Save name into first_name field
            user.email = form.cleaned_data['email']
            user.save()
            return redirect('signin')  # after signup, go to signin page
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

