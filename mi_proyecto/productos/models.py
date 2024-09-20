from mongoengine import Document, StringField, DecimalField, IntField

class Producto(Document):
    nombre = StringField(max_length=100)
    sabor = StringField(max_length=50)
    precio = DecimalField()
    cantidad = IntField()

    meta = {'collection': 'productos'}  # Especifica la colección correcta

    def __str__(self):
        return self.nombre
