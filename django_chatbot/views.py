from django.shortcuts import render, redirect
from django.http import JsonResponse
import openai
import os
import time
from django.http import HttpResponse 
from django.template import loader

from django.contrib import auth
from django.contrib.auth.models import User
from .models import Chat
from collections import deque


from django.utils import timezone
from datetime import datetime, timedelta

my_api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = my_api_key

RATE_LIMIT = 5
RATE_LIMIT_PERIOD = 30

# Track the timestamps of recent requests
request_timestamps = deque()

def ask_openai(user_message):
    # Current time
    now = datetime.now()
    
    # Remove timestamps that are outside the rate limit period
    while request_timestamps and (now - request_timestamps[0]).total_seconds() > RATE_LIMIT_PERIOD:
        request_timestamps.popleft()

    # Check if the rate limit has been exceeded
    if len(request_timestamps) >= RATE_LIMIT:
        retry_after = RATE_LIMIT_PERIOD - (now - request_timestamps[0]).total_seconds()
        rate_limit_error = f"Rate limit exceeded. Retrying after {retry_after:.2f} seconds."
        time.sleep(retry_after)
        return ask_openai(rate_limit_error)
    
     # Make the API request
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message}
            ]
        )
    
    # Add the current request timestamp to the queue
        request_timestamps.append(now)
        
        # Extract and return the answer
        answer = response.choices[0].message['content']
        return answer
    except openai.error.RateLimitError as e:
        retry_after = int(e.headers.get('Retry-After', 60))  # Default to 60 seconds if header is not available
        print(f"API rate limit exceeded. Retrying after {retry_after} seconds.")
        time.sleep(retry_after)
        return ask_openai(user_message)
    except Exception as e:
        return str(e)

# Create your views here.
def django_chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)

        return JsonResponse({'message': message, 'response': response})
    return render(request, 'chatrjp.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('django_chatbot')
        else:
            error_message = 'Invalid username or password'
            return render(request, 'signin.html', {'error_message': error_message})
    else:
        return render(request, 'signin.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            try:
                user = User.objects.create_user(username, email, password1)
                user.save()
                auth.login(request, user)
                return redirect('django_chatbot')
            except:
                error_message = 'Error creating account'
                return render(request, 'register.html', {'error_message': error_message})
        else:
            error_message = 'Password dont match'
            return render(request, 'register.html', {'error_message': error_message})
    return render(request, 'register.html')

def signout(request):
    auth.logout(request)
    return redirect('signin')

def users(request):
  user_data = User.objects.all()
  context = {
      'user_data' : user_data
  }
  return render(request, 'users.html', context)
