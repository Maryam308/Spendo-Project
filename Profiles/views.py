import bcrypt
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from pymongo import MongoClient
from django.conf import settings
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
  
        else:
            return redirect('login')  # If login fails, reload login page with error

    return render(request, 'registration/login.html')

def signup_view(request):
    error_message = ""
    username = request.POST.get('username', '')
    email = request.POST.get('email', '')
    password = request.POST.get('password', '')
    confirm_password = request.POST.get('confirm_password', '')

    if request.method == 'POST':
        # Check if password and confirm password match
        if password != confirm_password:
            error_message = "Passwords do not match. Please try again."
            password = confirm_password = ''  # Clear password fields
        else:
            # Check if the user already exists
            existing_user = users_collection.find_one({'username': username})
            existing_email = users_collection.find_one({'email': email})

            if existing_user and existing_email:
                error_message = "Both username and email are already in use. Please choose another."
            elif existing_user:
                error_message = "Username already exists. Please choose another username."
            elif existing_email:
                error_message = "Email is already in use. Please choose another email."
            else:
                # Hash the password and insert new user into MongoDB
                hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
                new_user = {
                    'username': username,
                    'email': email,
                    'password': hashed_password
                }
                users_collection.insert_one(new_user)
                return redirect('profiles:login')

    return render(request, 'registration/signup.html', {
        'error_message': error_message,
        'username': username,
        'email': email,
        'password': password,
        'confirm_password': confirm_password,
    })
