from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:list')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form':form})

class UserLoginView(LoginView):
    template_name = 'accounts/login.html'

class UserLogoutView(LogoutView):
    template_name = 'accounts/logout.html'
