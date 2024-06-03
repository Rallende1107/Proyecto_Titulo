class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        if 'carrito' not in self.session:
            self.session['carrito'] = {}
        self.carrito = self.session['carrito']

    def agregar(self, producto):
        print("Llamada a la función agregar")
        id = str(producto.id)
        if id not in self.carrito.keys():
            self.carrito[id] = {
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "cantidad": 1,
                "precio_unitario": producto.precio,
            }
        else:
            self.carrito[id]["cantidad"] += 1
        self.guardar_carrito()

    def guardar_carrito(self):
        print("Llamada a la función guardar_carrito")
        self.session['carrito'] = self.carrito
        self.session.modified = True

    def eliminar(self, producto):
        print("Llamada a la función eliminar")
        id = str(producto.id)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    def restar(self, producto):
        print("Llamada a la función restar")
        id = str(producto.id)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
            if self.carrito[id]["cantidad"] <= 0:
                self.eliminar(producto)
            self.guardar_carrito()

    def limpiar(self):
        print("Llamada a la función limpiar")
        self.session['carrito'] = {}
        self.session.modified = True
