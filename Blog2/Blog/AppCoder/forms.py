from django.forms import Form, CharField

class FutbolistaForm(Form):
    nombre = CharField()
    club = CharField()
    
class BasquetbolistaForm(Form):
    nombre = CharField()
    club = CharField()
    
class RugbierForm(Form):
    nombre = CharField()
    club = CharField()