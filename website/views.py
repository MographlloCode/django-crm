from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record

def home(request):
    ''' Home Page View ''' 
    
    records = Record.objects.all()
    records_total = len(records)
    
    # Check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have been logged in!')
            return redirect('home')
        else:
            messages.success(request, 'There was an error logging in, please, try again...')
            return redirect('home')
    
    return render(request, 'home.html', {'records': records, 'clients_ammount':records_total})

def logout_user(request):
    ''' Logout User '''
    logout(request)
    messages.success(request, 'You have been logged out!')
    return redirect('home')

def register_user(request):
    ''' Register User View '''
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and Login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You have successfully registered! Welcome!')
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})
    
    return render(request, 'register.html', {'form': form})
    
def customer_record(request, pk):
    ''' Customer Record View '''
    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'record': record})
    
    messages.success(request, 'You must be logged in to view that page...')
    return render(request, 'home.html', {})

def delete_record(request, pk):
    ''' Delete Customer View '''
    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        record.delete()
        messages.success(request, 'You have deleted the record successfully!')
        return redirect('home')
    
    messages.success(request, 'You must be logged to perform this action...')
    return render(request, 'home.html', {})
    