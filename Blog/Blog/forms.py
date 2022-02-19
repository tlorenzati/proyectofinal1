from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import EmailField, CharField, PasswordInput

class UserRegisterForm(UserCreationForm):
    email = EmailField
    password1 = CharField(label='Contraseña', widget=PasswordInput)
    password1 = CharField(label='Repetir Contraseña', widget=PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:'' for k in fields }
        

class UserEditForm(UserCreationForm):
    email = EmailField
    password1 = CharField(label='Contraseña', widget=PasswordInput)
    password1 = CharField(label='Repetir Contraseña', widget=PasswordInput)
    first_name = CharField()
    last_name = CharField()
    
    
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name']
        help_texts = {k:'' for k in fields }
        

