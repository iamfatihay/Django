from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import UserForm
from django.contrib.auth import login, logout
from django.contrib import messages


# Create your views here.
def register(request):

    # form=UserCreationForm()
    form=UserForm()

    if request.method=='POST':
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,'register successfully')
            return redirect("home")
        
    context={
        'form':form
    }
    return render(request,'users/register.html',context)




def user_login(request):
    
    form=AuthenticationForm(data=request.POST)
    if form.is_valid():
        user=form.get_user()
        login(request,user)
        messages.success(request,'login successfully')
        return redirect('home')
    context={
        'form':form
    }
    return render(request,'users/login.html',context)

def user_logout(request):
    logout(request)
    messages.warning(request,'logout successfully')
    return redirect('home')
   