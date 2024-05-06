from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator


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

    class Meta:
        db_table = 'Usuario'
        managed = True
        constraints = [
            # models.UniqueConstraint(fields=['username', 'cliente', 'comerciante'], name='unique_username_for_user_type')
        ]


    def clean(self):
        super().clean()
        if Usuario.objects.filter(username=self.username, cliente=self.cliente, comerciante=self.comerciante).exists():
            raise ValidationError("Este nombre de usuario ya está en uso para este tipo de usuario.")



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

    class Meta:
        db_table = 'Producto'
        managed = True
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

