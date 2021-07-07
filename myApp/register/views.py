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
