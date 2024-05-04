from django.shortcuts import render, redirect

# Create your views here.

from django.contrib.auth import authenticate, login
from .forms import ClienteForm, ComercianteForm


from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
# from .forms import User1CreationForm, User2CreationForm, User1LoginForm, User2LoginForm

# class User1RegisterView(CreateView):
#     template_name = 'user1_register.html'
#     form_class = User1CreationForm

#     def form_valid(self, form):
#         # Crea una instancia del modelo User1 y guarda los datos del formulario
#         user = form.save(commit=False)
#         user.is_user1 = True
#         user.save()
#         return redirect('user1_dashboard')  # Redirige a la página de dashboard de User1

# class User2RegisterView(CreateView):
#     template_name = 'user2_register.html'
#     form_class = User2CreationForm

#     def form_valid(self, form):
#         # Crea una instancia del modelo User2 y guarda los datos del formulario
#         user = form.save(commit=False)
#         user.is_user2 = True
#         user.save()
#         return redirect('user2_dashboard')  # Redirige a la página de dashboard de User2



# class User1LoginView(LoginView):
#     template_name = 'user1_login.html'
#     authentication_form = User1LoginForm

# class User2LoginView(LoginView):
#     template_name = 'user2_login.html'
#     authentication_form = User2LoginForm
