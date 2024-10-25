import bcrypt
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib import messages
from pymongo import MongoClient
from django.conf import settings
from django.contrib.auth.hashers import make_password
from db_connection import db
from db_connection import users_collection

users_collection = db['users_authentication'] 

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  # Log in the user
            return redirect('dashboard')  
        else:
            messages.error(request, 'Invalid username or password')  # Optional error message
            return redirect('login')  # If login fails, reload login page with error

    return render(request, 'registration/login.html')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password').encode('utf-8')

        # Check if the user already exists
        existing_user = users_collection.find_one({'username': username})
        existing_email = users_collection.find_one({'email': email})

        if existing_user and existing_email:
            messages.error(request, "Both username and email are already in use. Please choose another.")
            return redirect('profiles:signup')

        elif existing_user:
            messages.error(request, "Username already exists. Please choose another username.")
            return redirect('profiles:signup')

        elif existing_email:
            messages.error(request, "Email is already in use. Please choose another email.")
            return redirect('profiles:signup')

        # Hash the password and insert new user into MongoDB
        hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
        new_user = {
            'username': username,
            'email': email,
            'password': hashed_password
        }
        users_collection.insert_one(new_user)
        messages.success(request, "Account created successfully!")
        return redirect('profiles:login')

    return render(request, 'registration/signup.html')