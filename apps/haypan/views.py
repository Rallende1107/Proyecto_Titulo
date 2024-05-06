from django.http import Http404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (CreateView, FormView, UpdateView, ListView, DeleteView, DetailView, TemplateView)

from .forms import (UsuarioForm,  LocalForm, ProductoForm)
from .models import Usuario, Local, Producto

# Create your views here.

class HomeView(TemplateView):
    template_name = "index.html"


class ComercianteRegisterView(CreateView):
    template_name = 'user_register.html'
    form_class = UsuarioForm
    success_url = reverse_lazy ("home")
    title = 'Registro comerciante'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context
    def form_valid(self, form):
        form.instance.cliente = True
        form.instance.comerciante = False
        return super().form_valid(form)

class ClienteRegisterView(CreateView):
    template_name = 'user_register.html'
    form_class = UsuarioForm
    success_url = reverse_lazy ("home")
    title = 'Registro Cliente'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context

    def form_valid(self, form):
        form.instance.cliente = True
        form.instance.comerciante = False
        return super().form_valid(form)

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

##########################################################################################################
########################### Locales
##########################################################################################################

class LocalCreateView(LoginRequiredMixin, CreateView):
    model = Local
    template_name = "p_add.html"
    form_class = LocalForm
    success_url = reverse_lazy ("local_list")
    cancel_url = reverse_lazy ("home")
    title= 'Crear Nuevo Local'

    def get_login_url(self):
        return reverse_lazy("login")
    # def form_valid(self, form):
    #     # Asignar el comerciante actual como representante del local
    #     form.instance.representante = self.request.user
    #     return super().form_valid(form)

    def form_valid(self, form):
        # Obtener el ID del usuario logueado
        representante_id = self.request.user.id
        # Asignar el ID del usuario como representante del local
        form.instance.representante_id = representante_id
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['cancel_url'] = self.cancel_url
        return context

class LocalUpdateView(LoginRequiredMixin, UpdateView):
    model = Local
    form_class = LocalForm
    success_url = reverse_lazy ("local_list")
    template_name = "p_add.html"
    title = 'Modificar Local'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['cancel_url'] =  self.success_url

        return context

class LocalListView(ListView, LoginRequiredMixin):
    """ Lista de Todos los Locales"""
    model = Local
    template_name = "List_v1.html"
    context_object_name = 'elementos'
    title = 'Lista de Locales'
    addURL = reverse_lazy('local_add')
    homeURL = reverse_lazy('home')

    def get_queryset(self):
        # Filtrar el queryset por el id del usuario logueado
        usuario_id = self.request.user.id
        return Local.objects.filter(representante_id=usuario_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['addURL'] = self.addURL
        context['homeURL'] = self.homeURL

        # Añadir el usuario logueado al contexto
        context['usuario_logueado'] = self.request.user

        return context

##########################################################################################################
########################### Locales
##########################################################################################################


class ProductoListView(ListView):
    """ Lista de Todos los Locales"""
    model = Producto
    template_name = "List.html"
    context_object_name = 'elementos'
    title = 'Lista de Locales'
    addURL = reverse_lazy('local_Add')
    homeURL = reverse_lazy('home')

    def get_queryset(self):
        return Local.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['addURL'] = self.addURL
        context['homeURL'] = self.homeURL
        return context

class ProductoCreateView(LoginRequiredMixin, CreateView):
    model = Producto
    template_name = "p_add.html"
    form_class = ProductoForm
    success_url = reverse_lazy ("home")
    title= 'Crear Nuevo Producto'

    def get_login_url(self):
        return reverse_lazy("login")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context
