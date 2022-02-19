from django.forms import model_to_dict
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from AppCoder.forms import FutbolistaForm, RugbierForm, BasquetbolistaForm
from AppCoder.forms import AvatarFormulario

from .models import Avatar, Basquetbolistas, Futbolistas, Rugbiers

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


def inicio(request):
    if request.user.is_authenticated:
        avatares = Avatar.objects.filter(user=request.user)
        if avatares:
            avatar_url = avatares.last().imagen.url
        else:
            avatar_url = ''
        
        return render(request, 'AppCoder/inicio.html', {'avatar_url': avatar_url})
    else:
        return render(request, 'AppCoder/inicio.html')

# def futbolistas(request):
#     return render(request, 'AppCoder/futbolistas.html', 
#                   {'futbolistas':Futbolistas.objects.all()})

# def rugbiers(request):
#     return render(request, 'AppCoder/rugbiers.html',
#                   {'rugbiers':Rugbiers.objects.all()})

# def basquetbolistas(request):
#     return render(request, 'AppCoder/basquetbolistas.html',
#                   {'basquetbolistas':Basquetbolistas.objects.all()})

def futbolistas_formulario(request):
    if request.method == 'POST':
        formulario = FutbolistaForm(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            Futbolistas.objects.create(nombre=data['nombre'], contenido=data['contenido'])
            return redirect('futbolistas')
    else:
        formulario = FutbolistaForm()
    return render (request, 'AppCoder/futbolistasFormulario.html', {'formulario': formulario})

def basquetbolista_formulario(request):
    if request.method == 'POST':
        formulario = BasquetbolistaForm(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            Basquetbolistas.objects.create(nombre=data['nombre'], contenido=data['contenido'])
            return redirect('basquetbolistas')
    else:
        formulario = BasquetbolistaForm()
    return render (request, 'AppCoder/basquetbolistasFormulario.html', {'formulario': formulario})

def rugbier_formulario(request):
    if request.method == 'POST':
        formulario = RugbierForm(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            Rugbiers.objects.create(nombre=data['nombre'], contenido=data['contenido'])
            return redirect('rugbiers')
    else:
        formulario = RugbierForm()
    return render (request, 'AppCoder/rugbiersFormulario.html', {'formulario': formulario})


def futbolistas_delete(request, id_futbolista):
    futbolista = Futbolistas.objects.get(id=id_futbolista)
    futbolista.delete()
    
    return redirect ('futbolistas')

def basquetbolistas_delete(request, id_basquetbolista):
    basquetbolista = Basquetbolistas.objects.get(id=id_basquetbolista)
    basquetbolista.delete()
    
    return redirect ('basquetbolistas')

def rugbiers_delete(request, id_rugbier):
    rugbier = Rugbiers.objects.get(id=id_rugbier)
    rugbier.delete()
    
    return redirect ('rugbiers')

def futbolistas_update(request, id_futbolista):
    futbolista = Futbolistas.objects.get(id=id_futbolista)
    if request.method == 'POST':
        formulario = FutbolistaForm(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            
            futbolista.nombre=data['nombre']
            futbolista.contenido=data['contenido']
            futbolista.save()
            return redirect('futbolistas')
    else:
        formulario = FutbolistaForm(model_to_dict(futbolista))
    return render (request, 'AppCoder/futbolistasFormulario.html', {'formulario': formulario})

def basquetbolistas_update(request, id_basquetbolista):
    basquetbolista = Basquetbolistas.objects.get(id=id_basquetbolista)
    if request.method == 'POST':
        formulario = BasquetbolistaForm(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            
            basquetbolista.nombre=data['nombre']
            basquetbolista.contenido=data['contenido']
            basquetbolista.save()
            return redirect('basquetbolistas')
    else:
        formulario = BasquetbolistaForm(model_to_dict(basquetbolista))
    return render (request, 'AppCoder/basquetbolistasFormulario.html', {'formulario': formulario})

def rugbiers_update(request, id_rugbier):
    rugbier = Rugbiers.objects.get(id=id_rugbier)
    if request.method == 'POST':
        formulario = RugbierForm(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            
            rugbier.nombre=data['nombre']
            rugbier.contenido=data['contenido']
            rugbier.save()
            return redirect('rugbiers')
    else:
        formulario = RugbierForm(model_to_dict(rugbier))
    return render (request, 'AppCoder/rugbiersFormulario.html', {'formulario': formulario})

class ContactoListView(LoginRequiredMixin,ListView):
    model = Futbolistas
    template_name='AppCoder/contacto.html'
    context_object_name=''
    
    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto["avatar_url"] = Avatar.objects.filter(user=self.request.user).last().imagen.url
        
        return contexto

class FutbolistaListView(LoginRequiredMixin, ListView ):
    model = Futbolistas
    template_name='AppCoder/futbolistas.html'
    context_object_name='futbolistas'
    
    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto["avatar_url"] = Avatar.objects.filter(user=self.request.user).last().imagen.url
        
        return contexto
    
    
class BasquetbolistaListView(LoginRequiredMixin,ListView):
    model = Basquetbolistas
    template_name='AppCoder/basquetbolistas.html'
    context_object_name='basquetbolistas'
    
    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto["avatar_url"] = Avatar.objects.filter(user=self.request.user).last().imagen.url
        
        return contexto
    
class RugbiersListView(LoginRequiredMixin,ListView):
    model = Rugbiers
    template_name='AppCoder/rugbiers.html'
    context_object_name='rugbiers'
    
    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto["avatar_url"] = Avatar.objects.filter(user=self.request.user).last().imagen.url
        
        return contexto
    

class FutbolistasCreateView(LoginRequiredMixin,CreateView):
    model = Futbolistas
    success_url= reverse_lazy('futbolistas')
    fields= ['nombre', 'contenido']
    template_name= 'AppCoder/futbolistas_form.html'
    
class BasquetbolistasCreateView(LoginRequiredMixin,CreateView):
    model = Basquetbolistas
    success_url= reverse_lazy('basquetbolistas')
    fields= ['nombre', 'contenido']
    template_name= 'AppCoder/basquetbolistas_form.html'

class RugbiersCreateView(LoginRequiredMixin,CreateView):
    model = Rugbiers
    success_url= reverse_lazy('rugbiers')
    fields= ['nombre', 'contenido']
    template_name= 'AppCoder/rugbiers_form.html'


class FutbolistasUpdateView(LoginRequiredMixin,UpdateView):
    model = Futbolistas
    success_url= reverse_lazy('futbolistas')
    fields= ['nombre', 'contenido']
    template_name= 'AppCoder/futbolistas_form.html'
    
class BasquetbolistasUpdateView(LoginRequiredMixin,UpdateView):
    model = Basquetbolistas
    success_url= reverse_lazy('basquetbolistas')
    fields= ['nombre', 'contenido']
    template_name= 'AppCoder/basquetbolistas_form.html'

class RugbiersUpdateView(LoginRequiredMixin,UpdateView):
    model = Rugbiers
    success_url= reverse_lazy('rugbiers')
    fields= ['nombre', 'contenido']
    template_name= 'AppCoder/rugbiers_form.html'


class FutbolistasDeleteView(LoginRequiredMixin,DeleteView):
    model = Futbolistas 
    success_url= reverse_lazy('futbolistas')
    # template_name = 'AppCoder/futbolistas_confirm_delete.html'

class BasquetbolistasDeleteView(LoginRequiredMixin,DeleteView):
    model = Basquetbolistas 
    success_url= reverse_lazy('futbolistas')
    # template_name = 'AppCoder/basquetbolistas_confirm_delete.html'
    
class RugbiersDeleteView(LoginRequiredMixin,DeleteView):
    model = Rugbiers 
    success_url= reverse_lazy('rugbiers')
    # template_name = 'AppCoder/rugbiers_confirm_delete.html'
    
@login_required
def agregar_avatar(request):
    if request.method =='POST':
        formulario = AvatarFormulario(request.POST, request.FILES)
        
        if formulario.is_valid():
            avatar = Avatar(user=request.user, imagen=formulario.cleaned_data['imagen'])
            avatar.save()
            return redirect ('inicio')
    else:
        formulario = AvatarFormulario()
        
    return render(request, 'AppCoder/crear_avatar.html', {'form': formulario})





    