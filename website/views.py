from django.shortcuts import render

def home(request):
    ''' Home Page View ''' 
    return render(request, 'home.html', {})