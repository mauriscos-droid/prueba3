class producto:
    def __init__(self,nom,precio_base,stock):
        self.nombre = nom
        self.price = precio_base
        self.stock = stock

    def pors(self,porcentaje):
        self.price*+porcentaje
        print(f"el nuevo precio es {self.price}")
    def actualizar_stock(self,cantidad):
        if (self.stock+cantidad)<0:
            print("No puedes tener stock negativo")
        else:
            self.stock+=cantidad
            print(f"El nuevo stock es {self.stock}")
            
class categoria():
    def __init__(self,nam):
        self.name_e = nam
        self.list = []
    def agregar_producto(self):
        self.list.append(producto)
        print(f"El producto {producto.__name__} se agrego a la lista")
        
