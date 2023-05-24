from django.shortcuts import render
import random

def about(request):
    return render(request, 'about.html')

def home(request):
    return render(request, 'home.html')

def password(request):
    characters = list('abcdefghijklmnñopqrstuvwxyz')
    generated_pass = ''

    # Detectando si el usuario quiere letras mayúsculas o no
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    # Agregando caracteres especiales
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_-+=[]{}<>,.?/:;|~'))

    # Agregando números
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    # Pasando a entero la longitud deseada
    length = int(request.GET.get('length'))

    for _ in range(length):
        generated_pass += random.choice(characters)

    return render(request, 'password.html', {'password': generated_pass})
