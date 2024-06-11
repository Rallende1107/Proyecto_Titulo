from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView

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
    path('password_change/', PasswordChangeView.as_view(
        template_name='password_change.html',
        success_url=reverse_lazy('password_change_done')
    ), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(
        template_name='password_change_done.html'
    ), name='password_change_done'),

    path('user_panel/', views.userPanel, name='user_panel'),
    path('booking/<int:usuario_id>/', views.booking, name='booking'),
    path('merchant_reserve/<int:reserva_id>/', views.merchant_reserve, name='merchant_reserve'),
    path('actualizar_estado/<int:reserva_id>/', views.actualizar_estado, name='actualizar_estado'),
]

