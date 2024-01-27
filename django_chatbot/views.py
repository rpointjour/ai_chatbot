from django.shortcuts import render, redirect
from django.http import JsonResponse
import openai


openai_api_key = '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'
openai.api_key = openai_api_key

def ask_openai(message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello!"}
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