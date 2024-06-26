from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator, MaxLengthValidator
from .models import Region, Comuna, Reserva, Usuario, Familiar, Local, Producto
from django.contrib.auth.forms import UserCreationForm

class RegionForm(forms.ModelForm):
    """Form definition for Region."""

    nombre = forms.CharField(
        max_length=30,
        required=True,
        validators=[MinLengthValidator(3), MaxLengthValidator(30)],
        label='Nombre de la Región *',
        help_text='minimo 3 caracteres maximo 30 caracteres',
        error_messages={
            'required': 'Este campo es obligatorio.',
            'min_length': 'El nombre de la región debe tener al menos 3 caracteres.',
            'max_length': 'El nombre de la región es demasiado largo.',
        },
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off' ,
                # 'style': 'width: 250px;',
                'placeholder': 'Ingrese el nombre del género',
                'type': 'text'
            }
        )
    )


    latitud = forms.DecimalField(
        label='Latitud',
        required=True,
        validators=[MinValueValidator(-999), MaxValueValidator(999)],
        help_text='Debe estar en el rango de -999 a 999.',
        error_messages={
            'required': 'La latitud es obligatoria.',
            'min_value': 'La latitud debe ser mayor que -999.',
            'max_value': 'La latitud debe ser menor que 999.'
        },
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off',
                'placeholder': 'Ingrese la latitud',
                'type': 'number'
            }
        )
    )

    longitud = forms.DecimalField(
        label='Longitud',
        required=True,
        validators=[MinValueValidator(-999), MaxValueValidator(999)],
        help_text='Debe estar en el rango de -999 a 999.',
        error_messages={
            'required': 'La longitud es obligatoria.',
            'min_value': 'La longitud debe ser mayor que -999.',
            'max_value': 'La longitud debe ser menor que 999.'
        },
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off',
                'placeholder': 'Ingrese la longitud',
                'type': 'number'
            }
        )
    )
    class Meta:
        """Meta definition for Regionform."""
        model = Region
        fields = ['nombre', 'latitud', 'longitud']

class ComunaForm(forms.ModelForm):
    nombre = forms.CharField(
        label='Nombre de la comuna',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off',
                'placeholder': 'Ingrese el nombre de la comuna',
                'type': 'text'
            }
        )
    )
    latitud = forms.DecimalField(
        label='Latitud',
        validators=[MinValueValidator(-90), MaxValueValidator(90)],
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off',
                'placeholder': 'Ingrese la latitud',
                'type': 'number',
                'step': 'any'  # Permite números decimales
            }
        )
    )
    longitud = forms.DecimalField(
        label='Longitud',
        validators=[MinValueValidator(-180), MaxValueValidator(180)],
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off',
                'placeholder': 'Ingrese la longitud',
                'type': 'number',
                'step': 'any'  # Permite números decimales
            }
        )
    )

    class Meta:
        model = Comuna
        fields = ['nombre', 'latitud', 'longitud', 'region']


class UsuarioForm(UserCreationForm):
    username = forms.CharField(
        label='Nombre de usuario',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off',
                'placeholder': 'Ingrese su nombre de usuario',
                'type': 'text'
            }
        )
    )
    email = forms.EmailField(
        label='Correo electrónico',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off',
                'placeholder': 'Ingrese su correo electrónico',
                'type': 'email'
            }
        )
    )
    first_name = forms.CharField(
        label='Nombre',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off',
                'placeholder': 'Ingrese su nombre',
                'type': 'text'
            }
        )
    )
    last_name = forms.CharField(
        label='Apellido paterno',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off',
                'placeholder': 'Ingrese su apellido paterno',
                'type': 'text'
            }
        )
    )
    apellido_materno = forms.CharField(
        label='Apellido materno',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off',
                'placeholder': 'Ingrese su apellido materno',
                'type': 'text'
            }
        )
    )
    comuna = forms.ModelChoiceField(
        queryset=Comuna.objects.all(),
        label='Comuna',
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off'
            }
        )
    )
    direccion = forms.CharField(
        label='Dirección',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off',
                'placeholder': 'Ingrese su dirección',
                'type': 'text'
            }
        )
    )
    rut = forms.CharField(
        label='RUT',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off',
                'placeholder': 'Ingrese su RUT',
                'type': 'text'
            }
        )
    )
    phone = forms.CharField(
        label='Teléfono',
        max_length=10,
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off',
                'placeholder': 'Ingrese su número de teléfono',
                'type': 'text'
            }
        )
    )
    password1 = forms.CharField(
        label='Contraseña',
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Ingresa tu contraseña'}),
    )

    password2 = forms.CharField(
        label='Confirmar Contraseña',
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirma tu contraseña'}),
    )
    cliente = forms.BooleanField(required=False, widget=forms.HiddenInput)
    comerciante = forms.BooleanField(required=False, widget=forms.HiddenInput)
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'first_name', 'last_name', 'apellido_materno', 'comuna', 'direccion', 'rut', 'phone',  'password1', 'password2','comerciante','cliente']

class FamiliarForm(forms.ModelForm):
    nombre = forms.CharField(
        label='Nombre',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off',
                'placeholder': 'Ingrese el nombre del familiar',
                'type': 'text'
            }
        )
    )
    apellido_paterno = forms.CharField(
        label='Apellido paterno',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off',
                'placeholder': 'Ingrese el apellido paterno del familiar',
                'type': 'text'
            }
        )
    )
    apellido_materno = forms.CharField(
        label='Apellido materno',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off',
                'placeholder': 'Ingrese el apellido materno del familiar',
                'type': 'text'
            }
        )
    )
    telefono = forms.CharField(
        label='Teléfono',
        max_length=10,
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off',
                'placeholder': 'Ingrese el número de teléfono del familiar',
                'type': 'text'
            }
        )
    )
    familia = forms.ModelChoiceField(
        queryset=Usuario.objects.filter(cliente=True) ,
        label='Familia',
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off'
            }
        )
    )

    class Meta:
        model = Familiar
        fields = ['nombre', 'apellido_paterno', 'apellido_materno', 'telefono', 'familia']

class LocalForm(forms.ModelForm):
    nombre = forms.CharField(
        label='Nombre del local',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off',
                'placeholder': 'Ingrese el nombre del local',
                'type': 'text'
            }
        )
    )
    comuna = forms.ModelChoiceField(
        # queryset=Comuna.objects.all(),
        queryset=Comuna.objects.all().order_by('nombre'),  # Ordenar las comunas alfabéticamente por su nombre
        label='Comuna',
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off'
            }
        )
    )
    direccion = forms.CharField(
        label='Dirección',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off',
                'placeholder': 'Ingrese la dirección del local',
                'type': 'text'
            }
        )
    )
    # representante = forms.ModelChoiceField(
    #     queryset=Usuario.objects.filter(comerciante=True),
    #     label='Representante',
    #     widget=forms.Select(
    #         attrs={
    #             'class': 'form-control',
    #             'autocomplete': 'off'
    #         }
    #     )
    # )

    class Meta:
        model = Local
        fields = ['nombre', 'comuna', 'direccion',] #'representante',]

class ProductoForm(forms.ModelForm):
    nombre = forms.CharField(
        label='Nombre del producto',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off',
                'placeholder': 'Ingrese el nombre del producto',
                'type': 'text'
            }
        )
    )
    descripcion = forms.CharField(
        label='Descripción',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off',
                'rows': 3,
                'placeholder': 'Ingrese una descripción del producto'
            }
        )
    )
    cantidad = forms.IntegerField(
        label='Cantidad',
        validators=[MinValueValidator(0)],
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off',
                'placeholder': 'Ingrese la cantidad disponible',
                'type': 'number',
                'required': True,
                'min': 0
            }
        )
    )
    precio = forms.DecimalField(
        label='Precio',
        validators=[MinValueValidator(0)],
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off',
                'placeholder': 'Ingrese el precio',
                'type': 'number',
                'step': '0.01',
                'required': True,
                'min': 0
            }
        )
    )
    imagen = forms.ImageField(
        label='Imagen',
        required=False,
        widget=forms.ClearableFileInput(
            attrs={
                'class': 'form-control-file',
                'accept': 'image/*',
            }
        )
    )
    local = forms.ModelChoiceField(
        queryset=Local.objects.all(),
        label='Local',
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off',
            }
        )
    )

    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'cantidad', 'precio', 'imagen', 'local']



class ReservaForm(forms.ModelForm):
    numeroOrden = forms.IntegerField(
        label='Número de Orden',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off',
                'placeholder': 'Ingrese el número de orden',
                'type': 'number',
                'required': True,
                'min': 0
            }
        )
    )
    fechaInicio = forms.DateField(
        label='Fecha de Inicio',
        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off',
                'placeholder': 'Ingrese la fecha de inicio',
                'type': 'date'
            }
        )
    )
    cliente = forms.ModelChoiceField(
        queryset=Usuario.objects.filter(cliente=True),
        label='Cliente',
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off',
            }
        )
    )
    productos = forms.ModelMultipleChoiceField(
        queryset=Producto.objects.all(),
        label='Productos',
        widget=forms.CheckboxSelectMultiple()
    )
    local = forms.ModelChoiceField(
        queryset=Local.objects.all(),
        label='Local',
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off',
            }
        )
    )
    estado = forms.ChoiceField(
        choices=Reserva.TIPO_CHOICES,
        label='Estado',
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off',
            }
        )
    )

    class Meta:
        model = Reserva
        fields = ['numeroOrden', 'fechaInicio', 'cliente', 'productos', 'local', 'estado']



from django import forms
from .models import Usuario

class EditProfileForm(forms.ModelForm):
    username = forms.CharField(
        label='Nombre de usuario',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off',
                'placeholder': 'Ingrese su nombre de usuario',
                'type': 'text'
            }
        )
    )
    email = forms.EmailField(
        label='Correo electrónico',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off',
                'placeholder': 'Ingrese su correo electrónico',
                'type': 'email'
            }
        )
    )
    first_name = forms.CharField(
        label='Nombre',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off',
                'placeholder': 'Ingrese su nombre',
                'type': 'text'
            }
        )
    )
    last_name = forms.CharField(
        label='Apellido paterno',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off',
                'placeholder': 'Ingrese su apellido paterno',
                'type': 'text'
            }
        )
    )
    apellido_materno = forms.CharField(
        label='Apellido materno',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off',
                'placeholder': 'Ingrese su apellido materno',
                'type': 'text'
            }
        )
    )
    comuna = forms.ModelChoiceField(
        queryset=Comuna.objects.all(),
        label='Comuna',
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off'
            }
        )
    )
    direccion = forms.CharField(
        label='Dirección',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off',
                'placeholder': 'Ingrese su dirección',
                'type': 'text'
            }
        )
    )
    rut = forms.CharField(
        label='RUT',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off',
                'placeholder': 'Ingrese su RUT',
                'type': 'text'
            }
        )
    )
    phone = forms.CharField(
        label='Teléfono',
        max_length=10,
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'autocomplete': 'off',
                'placeholder': 'Ingrese su número de teléfono',
                'type': 'text'
            }
        )
    )

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'first_name', 'last_name', 'apellido_materno', 'comuna', 'direccion', 'rut', 'phone']



