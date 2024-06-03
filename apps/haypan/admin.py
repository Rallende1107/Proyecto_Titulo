from django.contrib import admin
# from import_export.admin import ImportExportModelAdmin
from .models import Region, Comuna, Reserva, Usuario, Familiar, Local, Producto

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    """Admin View for Region"""
    list_display = ('nombre', 'latitud', 'longitud')
    search_fields = ('nombre',)
    list_filter = ('nombre',)
    ordering = ('nombre',)

@admin.register(Comuna)
class ComunaAdmin(admin.ModelAdmin):
    """Admin View for Comuna"""
    list_display = ('nombre', 'latitud', 'longitud', 'region')
    search_fields = ('nombre',)
    list_filter = ('nombre', 'region')
    ordering = ('nombre',)

@admin.register(Usuario)
class UserAdmin(admin.ModelAdmin):
    """Admin View for Cliente"""
    list_display = ('username', 'email', 'first_name', 'last_name', 'apellido_materno', 'comuna', 'direccion', 'rut')
    search_fields = ('username', 'email', 'first_name', 'last_name', 'apellido_materno', 'comuna', 'direccion', 'rut')
    list_filter = ('comuna',)
    ordering = ('username',)


@admin.register(Familiar)
class FamiliarAdmin(admin.ModelAdmin):
    """Admin View for Familiar"""
    list_display = ('nombre', 'apellido_paterno', 'apellido_materno', 'telefono', 'familia')
    search_fields = ('nombre', 'apellido_paterno', 'apellido_materno', 'telefono', 'familia')
    list_filter = ('familia',)
    ordering = ('nombre',)

@admin.register(Local)
class LocalAdmin(admin.ModelAdmin):
    """Admin View for Local"""
    list_display = ('nombre', 'comuna', 'direccion', 'representante')
    search_fields = ('nombre', 'comuna', 'direccion', 'representante')
    list_filter = ('comuna',)
    ordering = ('nombre',)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    """Admin View for Producto"""
    list_display = ('nombre', 'descripcion', 'cantidad', 'precio', 'imagen', 'local')
    search_fields = ('nombre', 'descripcion', 'local')
    list_filter = ('local',)
    ordering = ('nombre',)

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('numeroOrden', 'fechaInicio', 'fecha_termino', 'cliente', 'local', 'estado', 'calcular_total')
    list_filter = ('estado', 'fechaInicio', 'local')
    search_fields = ('numeroOrden', 'cliente__username', 'local__nombre')
    date_hierarchy = 'fechaInicio'
    ordering = ('-fechaInicio',)
    filter_horizontal = ('productos',)

    def fecha_termino(self, obj):
        return obj.fecha_termino()
    fecha_termino.short_description = 'Fecha de Término'