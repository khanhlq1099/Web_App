from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib.auth import login
from django.contrib import messages


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request, "Registration successful." )
            return  redirect("/")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = RegisterForm()
    return render(request,"register/register.html",{"form":form})