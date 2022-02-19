
from django.db.models import Model, ForeignKey, CASCADE, ImageField
from django.db.models.fields import CharField
from django.contrib.auth.models import User





class Futbolistas(Model):
    nombre = CharField(max_length=40)
    contenido = CharField(max_length=40000)
    
    def __str__(self):
        return f'Nombre: {self.nombre} -----> CONTENIDO:{self.contenido}'
    
        
class Rugbiers(Model):
    nombre = CharField(max_length=40)
    contenido = CharField(max_length=40000)
    
    def __str__(self):
        return f'Nombre: {self.nombre} -----> CONTENIDO: {self.contenido}'
    
    
class Basquetbolistas(Model):
    nombre = CharField(max_length=40)
    contenido= CharField(max_length=40000)
    
    def __str__(self):
        return f'NOMBRE: {self.nombre} -----> CONTENIDO: {self.contenido}'
    
    
class Avatar(Model):
    user = ForeignKey(User, on_delete=CASCADE)
    imagen = ImageField(upload_to='avatares', null=True, blank=True)
    
    
    
    

