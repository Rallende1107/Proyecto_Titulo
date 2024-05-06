from django.http import Http404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (CreateView, FormView, UpdateView, ListView, DeleteView, DetailView, TemplateView)

from .forms import (ClienteForm, ComercianteForm, LocalForm, ProductoForm)
from .models import Cliente, Comerciante, Local, Producto

# Create your views here.

class HomeView(TemplateView):
    template_name = "index.html"


class ComercianteRegisterView(CreateView):
    template_name = 'user_register.html'
    form_class = ClienteForm
    success_url = reverse_lazy ("home")
    title = 'Registro comerciante'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context


    def form_valid(self, form):
        # Crea una instancia del modelo Cliente y guarda los datos del formulario
        user = form.save(commit=False)
        user.save()
        return super().form_valid(form)  # Devuelve la URL de éxito predeterminada

class ClienteRegisterView(CreateView):
    template_name = 'user_register.html'
    form_class = ClienteForm
    success_url = reverse_lazy ("home")
    title = 'Registro Cliente'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context


    def form_valid(self, form):
        # Crea una instancia del modelo Cliente y guarda los datos del formulario
        user = form.save(commit=False)
        user.save()
        return super().form_valid(form)  # Devuelve la URL de éxito predeterminada

class LoginView(FormView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    title = "Login"
    success_url = reverse_lazy ("home")

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)

        if user is not None:
            login(self.request, user)
            if isinstance(user, Cliente):
                return reverse_lazy ("home") # Clientes
            elif isinstance(user, Comerciante):
                return reverse_lazy ("home") # Comerciantes
            else:
                return redirect(self.success_url)
        else:
            return render(self.request, self.template_name, {'form': form, 'error': 'Usuario o contraseña incorrectos'})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

def salir(request):
    logout(request)
    return redirect('home')

# productos

class ComercianteRequiredMixin(LoginRequiredMixin):
    """Mixin que requiere que el usuario sea un comerciante."""
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()

        if not isinstance(request.user, Comerciante):
            raise Http404("No tienes permisos para acceder a esta página.")

        return super().dispatch(request, *args, **kwargs)

class LocalCreateView(ComercianteRequiredMixin, CreateView):
    model = Local
    template_name = "p_add.html"
    form_class = LocalForm
    success_url = reverse_lazy ("home")
    title= 'Crear Nuevo Local'
    # login_url = reverse_lazy ("login")

    def get_login_url(self):
        return reverse_lazy("login")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

class LocalUpdateView(ComercianteRequiredMixin, UpdateView):
    model = Local
    form_class = LocalForm
    success_url = reverse_lazy ("home")
    template_name = "p_add.html"
    title = 'Modificar Local'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['cancel_url'] =  self.success_url

        return context








class ProductoCreateView(ComercianteRequiredMixin, CreateView):
    model = Producto
    template_name = "p_add.html"
    form_class = ProductoForm
    success_url = reverse_lazy ("home")
    title= 'Crear Nuevo Producto'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context
