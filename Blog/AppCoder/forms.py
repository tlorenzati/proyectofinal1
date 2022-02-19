from django.forms import Form, CharField, ImageField

class FutbolistaForm(Form):
    nombre = CharField()
    contenido = CharField()
    
class BasquetbolistaForm(Form):
    nombre = CharField()
    contenido = CharField()
    
class RugbierForm(Form):
    nombre = CharField()
    contenido = CharField()
    
class AvatarFormulario(Form):
    imagen = ImageField(required=True)
