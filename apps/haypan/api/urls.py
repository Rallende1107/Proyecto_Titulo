from django.urls import path
from apps.haypan.api.api import User_api_view, user_detail_view
from apps.haypan.api.views.general_views import (
    ProductoCreateAPIView,
    ProductoListAPIView,
    ProductoRetrieveAPIView,
    ProductoDestroyAPIView,
    ProductoUpdateAPIView,
    ProductoListCreateAPIView,
    ProductoRetrieveUpdateDestroyAPIView,
    UserListCreateAPIView,
    UserRetrieveDestroyAPIView,
    LocalListCreateAPIView,
    LocalRetrieveDestroyAPIView,
    FamiliaListCreateAPIView,
    FamiliaRetrieveDestroyAPIView,

)

urlpatterns = [
    #path('usuario/', User_api_view, name='usuario_api'),
    #path('usuario/<int:pk>', user_detail_view, name='usuario_detail_api_view'),
    #path('producto/list/', ProductoListAPIView.as_view(), name='producto_api_list'),
    #path('producto/create/', ProductoCreateAPIView.as_view(), name='producto_api_create'),
    #path('producto/retrieve/<int:pk>/', ProductoRetrieveAPIView.as_view(), name='producto_api_retrieve'),
    #path('producto/destroy/<int:pk>/', ProductoDestroyAPIView.as_view(), name='producto_api_destroy'),
    #path('producto/update/<int:pk>/', ProductoUpdateAPIView.as_view(), name='producto_api_Update'),
    path('producto/', ProductoListCreateAPIView.as_view(), name='producto-list-create'),
    path('usuario/', UserListCreateAPIView.as_view(), name='usuario_list_create'),
    path('producto/<int:pk>/', ProductoRetrieveUpdateDestroyAPIView.as_view(), name='producto-retrieve-destroy-Update'),
    path('usuario/<int:pk>/', UserRetrieveDestroyAPIView.as_view(), name='usuario-retrieve-destroy-Update'),
    path('local/<int:pk>/', LocalRetrieveDestroyAPIView.as_view(), name='local-retrieve-destroy-Update'),
    path('familia/<int:pk>/', FamiliaRetrieveDestroyAPIView.as_view(), name='familia-retrieve-destroy-Update'),
    path('familia/', FamiliaListCreateAPIView.as_view(), name='familia-list-create'),
    path('local/', LocalListCreateAPIView.as_view(), name='local-list-create'),
    
]
