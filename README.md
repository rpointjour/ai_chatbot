# ChatRJP

<img src="https://github.com/rpointjour/ai_chatbot/assets/54840122/6828c10e-6a14-41e2-933d-4183416745df" alt="Chatbot" style="width:70%;height:70%;" />

#
**Description:** 

- **ChatRJP** (<i>"A  Chatbot Clone of ChatGPT"</i>) is a virtual chat application.
- <i>My version of ChatGPT</i> using the Python backend framework Django and utilizing OpenAI's API: <i>Chat Completion, GPT3.5-Turbo Language Model</i>
#
<i>Inspiration:</i> <i>https://github.com/tomitokko/django-chat-app</i> 

<i>References:</i>

- https://platform.openai.com/docs/guides/text-generation
- https://platform.openai.com/docs/api-reference/introduction

#
# Deployment (PythonAnyWhere)

- **ChatRJP url:** https://rjpking92.pythonanywhere.com

#
# ChatRJP 1.0

<img src="https://github.com/rpointjour/ai_chatbot/assets/54840122/b3bab735-d8fe-40b2-8e21-c7ddcd6dd0d3" alt="Chatbot" style="width:70%;height:70%;" />

#
# Project Setup

- **Virtual Environment** = `(chatbot)`
- **Django Project** = `/djangochat`
- **Django App** = `/django_chatbot`
#
# Templates

- `chatrjp_frame.html`
   - This is the **base template** for ChatRJP.
   - Includes links and scripts for **jQuery, cloudflare, and bootstrap**
   - Every other template extends from this one using `{% extends 'chat_frame.html' %}`
- `chatrjp.html`
  
  <img src="https://github.com/rpointjour/ai_chatbot/assets/54840122/bb8c9864-4e26-4f9b-b849-4f703e057be7" alt="Chatbot" style="width:70%;height:70%;" />

  - The template that ChatRJP is rendered from.
  - `{% extends 'chat_frame.html' %}`
  - `{% load static %}`: To load static files (images, favicon)
  - `{% block styles %}`: <style>...</style> : `{% endblock %}` --> Class styles are placed in this block
  - `{% block content %}`: <div>...</div> : `{% endblock %}` --> Main code for ChatRJP is written in this block
  - `<script>..</script>`
  - Implements use of the **fetch API call:** `fetch()`
  - This script **sends a POST request** to the server with a **CSRF token** and a message.
  - Then processes the response from the server, creates a new list item element to display the message, and appends it to the message list in the DOM.

- `signin.html`
 
    <img src="https://github.com/rpointjour/ai_chatbot/assets/54840122/1b2d7ecb-86ce-40a9-ae92-7f01db1918ea" alt="Chatbot" style="width:70%;height:70%;" />

    - Signin page for registered user
    - Once the user signs in they are redirected to the ChatRJP Application and can interact with the OpenAI API.
    
- `register.html`
 
    <img src="https://github.com/rpointjour/ai_chatbot/assets/54840122/758d6c11-8324-46bb-b657-b76d1a6f2e46" alt="Chatbot" style="width:70%;height:70%;" />

    - Account registration page
    - User info is stored into the database
    - Once authenticated the new user is automatically signed into the ChatRJP application upon successful registration.
# 
# Views

- `views.py`
   - `def django_chatbot(request):`
   - Upon a user posting their message, this method gets the user's message and returns a response from the OpenAI API call
   - `def ask_openai(message):`
   - The message is returned as a JSON response
   - The response (**from "ChatRJP"**) is then rendered to the chatrjp template for the user to see.
   - Returns a rate limit error if rate limit is exceeded (<i>Current limit: 5 requests within 30 secs</i>)
   - `def signin(request):`
   - **If** the user is successfully authenticated they will be redirected to the "django_chatbot" view (ChatRJP page).
   - **Else** an error message will be displayed and the will not be able to sign into ChatRJP.
   - `def register(request):`
   - Once the post request is received from the user this method checks if password1(password) and password2(confirm password) matches
   - `if password1 == password2`:
   - **Try** to save, authenticate the new user, and redirect them to the ChatRJP page.
   - **Except** when there is an error in creating the account.
   - `else:`
   - Passwords do not match and the user remains on the registration page with the error message displayed.
   - `def signout(request):`
   - Upon request redirect back to the sigin page
   - `def users(request):`
   - Keep track of **ChatRJP users** (usernames & emails, **exclude passwords**) and display in users template.
#
# Important Requirements
- `pip install`
- **openai v. 0.28.0** (API call does not work for v.1.0+)
- **python-dotenv** for using environment variables (i.e. OPENAI_API_KEY)
#
# Future of ChatRJP
- Version 1.0
  - <i>Text generation</i> ✅
- For version 2.0
   - **Image generation**
   - **Vision** (For understanding images)
- For version 3.0
    - **Text-to-speech**
    - **Speech-to-text**
