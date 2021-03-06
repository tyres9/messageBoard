from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib.auth import logout

def register(request):
    if request.user.is_authenticated:
        return redirect('logout')
  
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}.You can login now.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'users/registration.html',{'form':form})



@login_required                #decorators(add functionality to the view)..prohibit going directly to profile page without logging in
def profile(request):
    return render(request,'users/my_profile.html')
