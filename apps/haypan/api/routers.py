from rest_framework.routers import DefaultRouter
from apps.haypan.api.views.general_views import ProductoViews

router = DefaultRouter()

router.register(r'producto',ProductoViews)


urlpatterns = router.urls