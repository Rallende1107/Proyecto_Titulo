"""
URL configuration for projectoWeb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from apps.haypan.api.base import LoginToken,LogoutToken,UserToken
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.haypan.urls')),
    path('api/', include('apps.haypan.api.routers')),
    path('loginToken/', LoginToken.as_view(),name='loginToken'),
    path('logoutToken/', LogoutToken.as_view(), name='logoutToken'),
    path('refresh-token/', UserToken.as_view(), name='refresh-token'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)