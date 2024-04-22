from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, HttpResponse
from .forms import *

from django.views import View
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.
class Default_User_Registeration_View(View):
    def get(self, request):
        return render(request, 'user_register.html', {'form': DefaultUserRegisterForm()})
    def post(self, request):
        form = DefaultUserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(self.request, user)
            return redirect('/myapp/dashboard/')
        else:
            return render(request, 'user_register.html', {'form': form})

class Login(LoginView):
    template_name='login.html'
    redirect_authenticated_user = True
    
    def form_valid(self, form):
        """Security check complete. Log the user in."""
        auth_login(self.request, form.get_user())
        messages.info(self.request, 'Logged in successfully')
        return HttpResponseRedirect(self.get_success_url())

class Logout(LogoutView):
    
    def post(self, request, *args, **kwargs):
        """Logout may be done via POST."""
        auth_logout(request)
        redirect_to = self.get_success_url()
        if redirect_to != request.get_full_path():
            # Redirect to target page once the session has been cleared.
            messages.info(request, 'You are logged out')
            return HttpResponseRedirect(redirect_to)
        return super().get(request, *args, **kwargs)