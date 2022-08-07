from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate

def login_user(request):
    
    return render(request,'users/login.html',{})