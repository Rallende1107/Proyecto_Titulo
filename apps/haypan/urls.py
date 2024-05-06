from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # Base
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
    # path(
    #     'logout/',
    #     LogoutView.as_view(),
    #     name='logout'),

path('logout/', views.salir, name='salir'),

    # Local
    path(
        'local/add/',
        views.LocalCreateView.as_view(),
        name='local_add'
        ),

    path(
        'local/<int:pk>/update/',
        views.LocalCreateView.as_view(),
        name='local_update'
        ),
    path(
        'local/<int:pk>/delete/',
        views.LocalCreateView.as_view(),
        name='local_Delete'
        ),
    path(
        'local/list/',
        views.LocalCreateView.as_view(),
        name='local_list'
        ),

    path(
        'local/<int:pk>/detail/',
        views.LocalCreateView.as_view(),
        name='local_Detail'
        ),


    path(
        'producto/add/',
        views.ProductoCreateView.as_view(),
        name='producto_add'
        ),
        path(
        'producto/list/',
        views.LocalCreateView.as_view(),
        name='producto_list'
        ),

    path(
        'producto/<int:pk>/update/',
        views.ProductoCreateView.as_view(),
        name='producto_update'
        ),
    path(
        'producto/<int:pk>/datail/',
        views.ProductoCreateView.as_view(),
        name='producto_detail'
        ),
    path(
        'producto/<int:pk>/delete/',
        views.ProductoCreateView.as_view(),
        name='producto_delete'
        ),

    # path('translator/<int:pk>/update/', views.TranslatorUpdateView.as_view(), name='TranslatorUpdate'),
]
