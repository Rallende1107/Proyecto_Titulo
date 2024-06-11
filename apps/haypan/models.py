from datetime import date, datetime, timedelta
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.forms import ValidationError
from django.forms import ValidationError



# Create your models here.

class Region(models.Model):
    nombre = models.CharField(max_length=50)
    latitud = models.DecimalField(max_digits=9, decimal_places=4)
    longitud = models.DecimalField(max_digits=9, decimal_places=4)
    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'Region'
        managed = True
        verbose_name = 'Region'
        verbose_name_plural = 'Regiones'

class Comuna(models.Model):
    nombre = models.CharField(max_length=50)
    latitud = models.DecimalField(max_digits=9, decimal_places=4)
    longitud = models.DecimalField(max_digits=9, decimal_places=4)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'Comuna'
        managed = True
        verbose_name = 'Comuna'
        verbose_name_plural = 'Comunas'

class Usuario(AbstractUser):
    # username = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    first_name = models.CharField('Nombre', max_length=100)
    last_name = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    direccion = models.CharField(max_length=150)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, blank=True, null=True)
    rut = models.CharField(max_length=15)
    cliente = models.BooleanField(default=False)
    comerciante = models.BooleanField(default=False)
    phone = models.CharField(max_length=15)

    class Meta:
        db_table = 'Usuario'
        managed = True
        constraints = [
            # models.UniqueConstraint(fields=['username', 'cliente', 'comerciante'], name='unique_username_for_user_type')
        ]


    def clean(self):
        super().clean()
        # Verifica la unicidad del nombre de usuario excluyendo el usuario actual
        if Usuario.objects.filter(username=self.username).exclude(pk=self.pk).exists():
            raise ValidationError("Este nombre de usuario ya está en uso.")
        # Verifica la unicidad del correo electrónico excluyendo el usuario actual
        if Usuario.objects.filter(email=self.email).exclude(pk=self.pk).exists():
            raise ValidationError("Este correo electrónico ya está en uso.")



    def __str__(self):

        return self.username




class Familiar(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10, null=True, blank=True)
    familia = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.familia.nombre} {self.nombre} {self.apellido_paterno} {self.apellido_materno}"

    class Meta:
        db_table = 'Familiar'
        managed = True
        verbose_name = 'Familiar'
        verbose_name_plural = 'Familiares'

class Local(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=90, null=False)
    representante = models.ForeignKey(Usuario, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"{self.representante.first_name} - {self.nombre}"

    class Meta:
        db_table = 'Local'
        managed = True
        verbose_name = 'Local'
        verbose_name_plural = 'Locales'


class Producto(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    descripcion = models.CharField(max_length=250, null=True, blank=True)
    cantidad = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    precio = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    imagen = models.ImageField(upload_to="Producto", null=True)
    local = models.ForeignKey(Local, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.nombre
    def get_imagen_url(self):
            if self.imagen:
                return self.imagen.url
            else:
                return None

    class Meta:
        db_table = 'Producto'
        managed = True
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

from django.utils import timezone
class Reserva(models.Model):
    numeroOrden = models.IntegerField(unique=True)
    fechaInicio = models.DateField()
    horaInicio = models.TimeField(default=timezone.now) 
    cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE, limit_choices_to={'cliente': True})
    productos = models.ManyToManyField(Producto)
    local = models.ForeignKey(Local, on_delete=models.CASCADE)

    SOLICITADO = '1'
    EN_ESPERA = '2'
    RETIRADO = '3'
    CANCELADO_CLIENTE = '4'
    CANCELADO_COMERCIANTE = '5'
    EXPIRADO = '6'

    TIPO_CHOICES = [
        (SOLICITADO, 'Solicitado'),
        (EN_ESPERA, 'En Espera'),
        (RETIRADO, 'Retirado'),
        (CANCELADO_CLIENTE, 'Cancelado Cliente'),
        (CANCELADO_COMERCIANTE, 'Cancelado Comerciante'),
        (EXPIRADO, 'Expirado'),
    ]

    estado = models.CharField(
        max_length=1, choices=TIPO_CHOICES, default=SOLICITADO)
    
    def cancelar_por_cliente(self):
        self.estado = self.CANCELADO_CLIENTE
        self.fecha_cancelado_cliente = datetime.now()
        self.save()

    def cancelar_por_comerciante(self):
        self.estado = self.CANCELADO_COMERCIANTE
        self.fecha_cancelado_comerciante = datetime.now()
        self.save()

    def marcar_como_retirado(self):
        self.estado = self.RETIRADO
        self.save()

    def marcar_como_en_espera(self):
        self.estado = self.EN_ESPERA
        self.save()

    def marcar_como_expirado(self):
        self.estado = self.EXPIRADO
        self.save()

    def fecha_termino(self):
        if self.estado == self.EXPIRADO:
            return datetime.now()  # Si está expirado, devuelve la fecha y hora actual
        else:
            return self.fechaInicio + timedelta(hours=4)  # De lo contrario, devuelve la fecha de inicio más 4 horas

    def __str__(self):
        return f"Reserva #{self.numeroOrden}"

    def calcular_total(self):
        total = sum(producto.precio * producto.cantidad for producto in self.productos.all())
        return total

    def clean(self):
        super().clean()
        if self.fechaInicio < date.today():
            raise ValidationError('La fecha de inicio no puede ser anterior a la fecha actual.')

    def save(self, *args, **kwargs):
        self.clean()  # Llama a clean() para validar antes de guardar
        super().save(*args, **kwargs)


class DetalleReserva(models.Model):
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Detalle de reserva #{self.reserva.numeroOrden} - Producto: {self.producto.nombre}"

    class Meta:
        db_table = 'DetalleReserva'
        managed = True
        verbose_name = 'Detalle de Reserva'
        verbose_name_plural = 'Detalles de Reserva'