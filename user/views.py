from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from user.forms import UserForm
from user.models import User

# Create your views here.

def login(request):
    return render(request, 'login.html')

def register(request):
    formulario = UserForm(request.POST or None)
    msg = ''
    if formulario.is_valid():
        formulario.save()
        formulario = UserForm()
        msg = 'Pedido realizado com sucesso'
    
    contexto = {
        'form' : formulario,
        'msg' : msg
    }
    return render(request, 'register.html', contexto)

def logout_request(request):
    logout(request)
    messages.info(request, "Você saiu da sua conta!")
    return redirect("home:index")