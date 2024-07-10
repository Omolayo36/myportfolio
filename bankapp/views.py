from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'bankapp/index.html', {})

def privacy_setting(request):
    return render(request, 'bankapp/privacy_setting.html', {} )

def dashboard_manu(request):
    return render(request, 'bankapp/dashboard_manu.html', {} )

def home_page(request):
    return render(request, 'bankapp/home_page.html', {} )

def calendar(request):
    return render(request, 'bankapp/calendar.html', {} )

def horizontal_menu(request):
    return render(request, 'bankapp/horizontal_menu.html', {} )

def horizontal_top_menu(request):
    return render(request, 'bankapp/horizontal_top_menu.html', {} )

def two_sidebar(request):
    return render(request, 'bankapp/two_sidebar.html', {} )

def vertical_top_menu(request):
    return render(request, 'bankapp/vertical_top_menu.html', {} )

def transfer(request):
    return render(request, 'bankapp/transfer.html', {} )

def transfer_options(request):
    return render(request, 'bankapp/transfer_options.html', {} )



def signup(request):
    if request.method == "POST":
        name = request.POST.get('name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        new_user = User.objects.create_user(username=username, email=email, password=password)
        new_user.first_name = name
        new_user.save()
        return redirect('signin')

    return render(request, 'bankapp/account/signup.html', {})

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']


        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_page')
        else:
            return HttpResponse('<h1 style="color:rgb(186, 4, 34); width:100%;text-align:center">Invalid Login</h1><br><h1 style="color:rgb(15, 15, 15); width:100%;text-align:center"><a style="text-decoration:none" class="btn btn-primary mt-3" href="login"><i class="ri-home-4-line"></i>Re-Login</a></h1>')

    return render(request, 'bankapp/account/signin.html', {})

@login_required
def account_dashboard(request):
    username = request.user.username
    return render(request, 'bankapp/dashboard/account_dashboard.html', {'username': username})


def logout(request):
    logout(request)
    return render(request, 'bankapp/account/signin.html', {})

