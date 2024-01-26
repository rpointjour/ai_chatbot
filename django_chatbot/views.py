from django.shortcuts import render

# Create my views here.

def django_chatbot(request):
    return render(request, 'chatbot.html')    # Render chatbot.html