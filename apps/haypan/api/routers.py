from rest_framework.routers import DefaultRouter
from apps.haypan.api.views.general_views import DetalleReservaViews, ProductoViews, ReservaViews,UsuarioViews,LocalViews,FamiliaViews,ComunaViews
FamiliaViews

router = DefaultRouter()

router.register(r'producto',ProductoViews),
router.register(r'usuario',UsuarioViews),
router.register(r'local',LocalViews),
router.register(r'familia',FamiliaViews),
router.register(r'comuna',ComunaViews),
router.register(r'reserva',ReservaViews),
router.register(r'detalleReserva',DetalleReservaViews),
urlpatterns = router.urls