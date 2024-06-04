from decimal import Decimal

def total_carrito(request):
    total = Decimal('0.00')  # Inicializa el total como Decimal
    if request.user.is_authenticated:
        carrito = request.session.get("carrito", {})
        for key, value in carrito.items():
            if isinstance(value, dict) and "precio" in value:
                precio = value.get("precio")
                try:
                    precio_decimal = Decimal(precio)
                    total += precio_decimal * value.get("cantidad", 1)  # Multiplica por la cantidad si está disponible
                except (TypeError, ValueError):
                    # Maneja el caso en el que el precio no es un número válido
                    pass
    return {"total_carrito": total}
