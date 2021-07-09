from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth

# Create your views here.
def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        passwordConfirmation = request.POST['confirm_password']
        
        if password == passwordConfirmation:
            if User.objects.filter(email = email).exists():
                messages.info(request,'Email already registered')
                return redirect('register')
            elif User.objects.filter(username = username).exists():
                messages.info(request,'Username already registered')
                return redirect('register')
            else: 
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'Passwords not match')
            
    return render(request,'register.html')

#login route
def login(request):
    if request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Cedentials no valid')
            return redirect('login')
    else:
        return render(request,'login.html')
    
def home(request):
    return render(request,'home.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('login')
    else:
        return render(request,'logout.html')