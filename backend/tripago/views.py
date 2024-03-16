from django.shortcuts import render, redirect
from . forms import CreateUserForm, LoginForm, ItineraryGenerationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# authentication models and functions
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout


def homepage(request):
    return render(request, 'tripago/index.html')


def register(request):
    form = CreateUserForm()
    
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        form = CreateUserForm(data = {
            'first_name': first_name,
            'last_name': last_name,
            'username': username,
            'email': email,
            'password1': password1,
            'password2': password2
        })

        if form.is_valid():
            form.save()

            return redirect('login')

    return render(request, 'tripago/register.html')


def login(request):
    form = LoginForm()

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        form = LoginForm(request, data={
            'username': username,
            'password': password
        
        })

        if form.is_valid():
            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)

                return redirect('dashboard')

    return render(request, 'tripago/login.html')


@login_required(login_url='login')
def dashboard(request):
    return render(request, 'tripago/dashboard.html')


def logout(request):
    auth.logout(request)
    return redirect("")


def create_itinerary(request):
    form = ItineraryGenerationForm()

    if request.method == "POST":
        city = request.POST.get('city')
        country = request.POST.get('country')

        form = ItineraryGenerationForm(data={
            'city': city, 
            'country': country
        })

        return HttpResponse(f"Your itinerary for {city} in {country} has been created successfully!")

    return render(request, 'tripago/create-itinerary.html')