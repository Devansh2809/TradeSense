from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

# Home View
@login_required
def home(request):
    return render(request, "home.html", {})

# Signup View
def authView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('home') 
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect('login')  
