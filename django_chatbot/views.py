from django.shortcuts import render, redirect
from django.http import JsonResponse
import openai
import os


my_api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = my_api_key

def ask_openai(user_message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_message}
        ]
    )
    
    answer = response.choices[0].message.content.strip()
    return answer

# Create your views here.
def django_chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)

        return JsonResponse({'message': message, 'response': response})
    return render(request, 'chatbot.html')