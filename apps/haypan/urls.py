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
    path('delete_product_cart-producto/<int:producto_id>/', views.delete_product_cart, name='delete_product_cart'),
    path('clean_cart-producto/', views.clean_cart, name='clean_cart'),
    path('cart/', views.cart, name='cart'),
    path('edit_cart/<int:producto_id>/', views.edit_cart, name='edit_cart'),
    path('reserva/', views.reserva, name='reserva'),
    path('my_reservations/', views.my_reservations, name='my_reservations'),
    path('my_reservations/<int:reserva_id>/', views.reservation_detail, name='reservation_detail'),
    path('cancelar_reserva/<int:reserva_id>/', views.cancelar_reserva, name='cancelar_reserva'),

    path('profile/', views.UserProfileView.as_view(), name='profile'),
    path('profile/edit/', views.UserProfileUpdateView.as_view(), name='edit_profile'),
]

