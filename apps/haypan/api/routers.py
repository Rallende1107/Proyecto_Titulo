from rest_framework.routers import DefaultRouter
from apps.haypan.api.views.general_views import ProductoViews,UsuarioViews,LocalViews,FamiliaViews,ComunaViews
FamiliaViews

router = DefaultRouter()

router.register(r'producto',ProductoViews),
router.register(r'usuario',UsuarioViews),
router.register(r'local',LocalViews),
router.register(r'familia',FamiliaViews),
router.register(r'comuna',ComunaViews),
urlpatterns = router.urls