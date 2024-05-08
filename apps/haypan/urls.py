from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # Base
    path(
        '',
        views.HomeView.as_view(),
        name='home'
        ),

    path(
        'home/',
        views.HomeView.as_view(),
        name='home'
        ),
    # Usuarios registro
    path(
        'registro/cliente/',
        views.ClienteRegisterView.as_view(),
        name='Register_Cliente'
        ),
    path(
        'registro/comerciante/',
        views.ComercianteRegisterView.as_view(),
        name='Register_Comerciante'
        ),
    # Usuarios Login
    path(
        'login/',
        views.LoginView.as_view(),
        name='login'
        ),
        path(
            'logout/',
            views.salir,
            name='salir'
        ),

    # Local
    path(
        'local/add/',
        views.LocalCreateView.as_view(),
        name='local_add'
        ),

    path(
        'local/<int:pk>/update/',
        views.LocalUpdateView.as_view(),
        name='local_update'
        ),
    path(
        'local/<int:pk>/delete/',
        views.LocalLDeleteView.as_view(),
        name='local_delete'
        ),
    path(
        'local/list/',
        views.LocalListView.as_view(),
        name='local_list'
        ),



    path(
        'producto/add/',
        views.ProductoCreateView.as_view(),
        name='producto_add'
        ),
        path(
        'producto/list/',
        views.ProductoListView.as_view(),
        name='producto_list'
        ),

    path(
        'producto/<int:pk>/update/',
        views.ProductoUpdateView.as_view(),
        name='producto_update'
        ),

    path(
        'producto/<int:pk>/delete/',
        views.ProductoDeleteView.as_view(),
        name='producto_delete'
        ),

]
