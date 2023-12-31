from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

# Create your views here.
def dashboard(request):
    return render(request, 'accounts/dashboard.html')

def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username existed!")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email existed!")
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username = username, password = password, email = email, 
                    first_name = first_name, last_name = last_name)
                user.save()
                messages.success(request, "You are now registered!")
                return redirect('login')
        else:
            messages.error(request, "Password do not match")
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')
    

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            # messages.success(request, 'You are login in !')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else: 
        return render(request, 'accounts/login.html')

def logout(request):
    auth.logout(request)
    return redirect('index')