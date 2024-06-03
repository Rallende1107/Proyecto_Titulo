from datetime import timezone
from django.conf import settings
from django.forms import ValidationError
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.utils.timezone import now
from django.views.generic import (CreateView, FormView, UpdateView, ListView, DeleteView, DetailView, TemplateView)
from .forms import (UsuarioForm,  LocalForm, ProductoForm)
from .models import Reserva, Usuario, Local, Producto
from django.contrib.auth.decorators import login_required
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
    cancel_url = reverse_lazy ("local_list")
    title= 'Crear Nuevo Local'

    def get_login_url(self):
        return reverse_lazy("login")

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
        context['success_url'] = self.success_url
        return context

class LocalUpdateView(LoginRequiredMixin, UpdateView):
    model = Local
    form_class = LocalForm
    success_url = reverse_lazy ("local_list")
    template_name = "p_add.html"
    title = 'Modificar Local'

    def get_login_url(self):
        return reverse_lazy("login")

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

    def get_login_url(self):
        return reverse_lazy("login")

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

class LocalLDeleteView(DeleteView, LoginRequiredMixin):
    model = Local
    template_name = "delete.html"
    success_url = reverse_lazy("local_list")
    title = 'Borrar Local'

    def get_login_url(self):
        return reverse_lazy("login")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categoria = self.get_object()  # Obtener la instancia de la marca
        context['mensaje'] = f"¿Estás seguro de que deseas eliminar el local: '{categoria.nombre}'?"
        context['mensaje_2'] = "¡Esta acción es irreversible!"
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context


##########################################################################################################
########################### Locales
##########################################################################################################


class ProductoListView(ListView):
    """ Lista de Todos los Productos"""
    model = Producto
    template_name = "List.html"
    context_object_name = 'elementos'
    title = 'Lista de Locales'
    addURL = reverse_lazy('local_Add')
    homeURL = reverse_lazy('producto_list')

    def get_queryset(self):
        return Producto.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['addURL'] = self.addURL
        context['homeURL'] = self.homeURL
        context['success_url'] = reverse_lazy('local_list')
        return context

class ProductoCreateView(LoginRequiredMixin, CreateView):
    model = Producto
    template_name = "p_add.html"
    form_class = ProductoForm
    success_url = reverse_lazy ("producto_list")
    title= 'Crear Nuevo Producto'

    def get_login_url(self):
        return reverse_lazy("login")

    def form_valid(self, form):

        return super().form_valid(form)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        context['success_url'] = self.success_url
        return context


class ProductoUpdateView(LoginRequiredMixin, UpdateView):
    model = Producto
    form_class = ProductoForm
    success_url = reverse_lazy ("producto_list")
    template_name = "p_add.html"
    title = 'Actualzar Producto'

    def get_login_url(self):
        return reverse_lazy("login")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['cancel_url'] =  self.success_url

        return context


class ProductoDeleteView(DeleteView, LoginRequiredMixin):
    model = Producto
    template_name = "delete.html"
    success_url = reverse_lazy("producto_list")
    title = 'Borrar Producto'

    def get_login_url(self):
        return reverse_lazy("login")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categoria = self.get_object()  # Obtener la instancia de la marca
        context['mensaje'] = f"¿Estás seguro de que deseas eliminar el Producto: '{categoria.nombre}'?"
        context['mensaje_2'] = "¡Esta acción es irreversible!"
        context['title'] = self.title
        context['cancel_url'] = self.success_url
        return context
    




from django.db.models import F



@login_required
def cart(request):
    if request.method == 'GET' and 'producto_id' in request.GET:
        producto_id = request.GET.get('producto_id')
        cantidad = int(request.GET.get('cantidad', 1))

        try:
            producto = Producto.objects.get(pk=producto_id)
            carrito = request.session.get('carrito', {})

            if producto_id in carrito:
                carrito[producto_id] += cantidad
            else:
                carrito[producto_id] = cantidad

            request.session['carrito'] = carrito
            request.session.modified = True

            return redirect(reverse('cart'))

        except Producto.DoesNotExist:
            return HttpResponse("Error: Producto no encontrado.", status=404)

    productos_en_carrito = []
    carrito = request.session.get('carrito', {})
    for producto_id, cantidad in carrito.items():
        producto = Producto.objects.get(pk=producto_id)
        producto.cantidad_en_carrito = cantidad
        productos_en_carrito.append(producto)

    total_precio = sum(producto.precio * producto.cantidad_en_carrito for producto in productos_en_carrito)

    return render(request, 'cart.html', {
        'productos_en_carrito': productos_en_carrito,
        'total_precio': total_precio
    })

def delete_product_cart(request, producto_id):
    if request.method == 'POST':
        carrito = request.session.get('carrito', {})
        if str(producto_id) in carrito:
            producto = get_object_or_404(Producto, pk=producto_id)
            producto.cantidad += carrito[str(producto_id)]
            producto.save()
            del carrito[str(producto_id)]
            request.session['carrito'] = carrito
    return HttpResponseRedirect(reverse('cart'))

def clean_cart(request):
    carrito = request.session.get("carrito", {})
    for producto_id, cantidad in carrito.items():
        producto = Producto.objects.get(pk=producto_id)
        producto.cantidad = F('cantidad') + cantidad
        producto.save(update_fields=['cantidad'])
    request.session.pop("carrito", None)
    request.session.modified = True
    return redirect('home')

def edit_cart(request, producto_id):
    if request.method == 'POST':
        nueva_cantidad = int(request.POST.get('cantidad', 1))

        try:
            producto = Producto.objects.get(pk=producto_id)
            carrito = request.session.get('carrito', {})
            cantidad_anterior = carrito.get(str(producto_id), 0)

            # Calcular la diferencia entre la nueva cantidad y la anterior
            diferencia = nueva_cantidad - cantidad_anterior

            # Verificar que la nueva cantidad sea válida
            if nueva_cantidad > 0:
                # Si hay una diferencia positiva, es un aumento en la cantidad del carrito
                if diferencia > 0:
                    # Verificar si hay suficiente stock disponible para el aumento
                    if producto.cantidad >= diferencia:
                        carrito[str(producto_id)] = nueva_cantidad
                        request.session['carrito'] = carrito
                        request.session.modified = True
                        # No actualizar el stock en la base de datos aquí
                        return redirect(reverse('cart'))
                    else:
                        return HttpResponse("Error: Cantidad insuficiente para agregar al carrito.", status=400)
                # Si hay una diferencia negativa, es una reducción en la cantidad del carrito
                elif diferencia < 0:
                    # No actualizar el stock en la base de datos aquí
                    carrito[str(producto_id)] = nueva_cantidad
                    request.session['carrito'] = carrito
                    request.session.modified = True
                    return redirect(reverse('cart'))
                else:
                    # Si no hay diferencia, no se requieren cambios
                    return redirect(reverse('cart'))
            else:
                return HttpResponse("Error: Cantidad inválida para actualizar el carrito.", status=400)
        except Producto.DoesNotExist:
            return HttpResponse("Error: Producto no encontrado.", status=404)

    return redirect('cart')


@login_required
def reserva(request):
    # Obtener el carrito de la sesión
    carrito = request.session.get('carrito', {})

    if not carrito:
        print("Error: El carrito está vacío.")
        return redirect(reverse('carrito'))  # Redirige al carrito si está vacío

    # Generar un número de orden único
    numero_orden = Reserva.objects.count() + 1

    # Obtener el primer local disponible (puedes ajustar esta lógica según tus necesidades)
    local = Local.objects.first()
    if not local:
        print("Error: No hay locales disponibles.")
        return redirect(reverse('cart'))

    # Crear una nueva reserva
    reserva = Reserva(
        numeroOrden=numero_orden,
        fechaInicio=now().date(),
        cliente=request.user,
        local=local,
        estado=Reserva.SOLICITADO  # '1' para "Solicitado"
    )

    try:
        reserva.clean()  
        reserva.save()

        
        for producto_id, cantidad in carrito.items():
            producto = Producto.objects.get(pk=producto_id)
            reserva.productos.add(producto)
            producto.cantidad -= cantidad
            producto.save()

        
        request.session['carrito'] = {}
        request.session.modified = True

        print(f"Reserva creada con ID: {reserva.id} para el cliente: {request.user.username}")

        return redirect(reverse('home'))  

    except ValidationError as e:
        print(f"Error al crear la reserva: {e.message_dict}")
        return redirect(reverse('cart'))  
    


def my_reservations(request):
    # Filtrar las reservas del usuario actual
    reservas = Reserva.objects.filter(cliente=request.user)
    return render(request, 'my_reservations.html', {'reservas': reservas})


def reservation_detail(request, reserva_id):
    reserva = get_object_or_404(Reserva, pk=reserva_id)
    return render(request, 'reservation_detail.html', {'reserva': reserva})
