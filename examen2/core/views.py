from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Pendiente
from .forms import PendienteForm

def index(request):
    """Vista principal del sistema de pendientes"""
    return render(request, 'core/core.html')

# Vista 1: Lista de todos los pendientes (solo IDs)
def pendientes_ids(request):
    """Lista de todos los pendientes mostrando solo IDs"""
    pendientes = Pendiente.objects.all()
    context = {
        'pendientes': pendientes,
        'titulo': 'Todos los Pendientes - Solo IDs',
        'vista': 'ids'
    }
    return render(request, 'core/pendientes_lista.html', context)

# Vista 2: Lista de todos los pendientes (IDs y Titles)
def pendientes_ids_titles(request):
    """Lista de todos los pendientes mostrando IDs y Títulos"""
    pendientes = Pendiente.objects.all()
    context = {
        'pendientes': pendientes,
        'titulo': 'Todos los Pendientes - IDs y Títulos',
        'vista': 'ids_titles'
    }
    return render(request, 'core/pendientes_lista.html', context)

# Vista 3: Lista de todos los pendientes sin resolver (ID y Title)
def pendientes_sin_resolver(request):
    """Lista de pendientes sin resolver mostrando ID y Título"""
    pendientes = Pendiente.objects.filter(resuelto=False)
    context = {
        'pendientes': pendientes,
        'titulo': 'Pendientes Sin Resolver - ID y Título',
        'vista': 'sin_resolver'
    }
    return render(request, 'core/pendientes_lista.html', context)

# Vista 4: Lista de todos los pendientes resueltos (ID y Title)
def pendientes_resueltos(request):
    """Lista de pendientes resueltos mostrando ID y Título"""
    pendientes = Pendiente.objects.filter(resuelto=True)
    context = {
        'pendientes': pendientes,
        'titulo': 'Pendientes Resueltos - ID y Título',
        'vista': 'resueltos'
    }
    return render(request, 'core/pendientes_lista.html', context)

# Vista 5: Lista de todos los pendientes (IDs y userID)
def pendientes_ids_users(request):
    """Lista de todos los pendientes mostrando IDs y userID"""
    pendientes = Pendiente.objects.all()
    context = {
        'pendientes': pendientes,
        'titulo': 'Todos los Pendientes - IDs y User IDs',
        'vista': 'ids_users'
    }
    return render(request, 'core/pendientes_lista.html', context)

# Vista 6: Lista de todos los pendientes resueltos (ID y userID)
def pendientes_resueltos_users(request):
    """Lista de pendientes resueltos mostrando ID y userID"""
    pendientes = Pendiente.objects.filter(resuelto=True)
    context = {
        'pendientes': pendientes,
        'titulo': 'Pendientes Resueltos - ID y User ID',
        'vista': 'resueltos_users'
    }
    return render(request, 'core/pendientes_lista.html', context)

# Vista 7: Lista de todos los pendientes sin resolver (ID y userID)
def pendientes_sin_resolver_users(request):
    """Lista de pendientes sin resolver mostrando ID y userID"""
    pendientes = Pendiente.objects.filter(resuelto=False)
    context = {
        'pendientes': pendientes,
        'titulo': 'Pendientes Sin Resolver - ID y User ID',
        'vista': 'sin_resolver_users'
    }
    return render(request, 'core/pendientes_lista.html', context)

# Vistas CRUD
@login_required
def crear_pendiente(request):
    """Vista para crear un nuevo pendiente"""
    if request.method == 'POST':
        form = PendienteForm(request.POST)
        if form.is_valid():
            pendiente = form.save(commit=False)
            pendiente.user = request.user
            pendiente.save()
            messages.success(request, 'Pendiente creado exitosamente.')
            return redirect('pendientes_ids_titles')
    else:
        form = PendienteForm()
    
    context = {
        'form': form,
        'titulo': 'Crear Nuevo Pendiente'
    }
    return render(request, 'core/crear_pendiente.html', context)

@login_required
def editar_pendiente(request, pendiente_id):
    """Vista para editar un pendiente existente"""
    pendiente = get_object_or_404(Pendiente, id=pendiente_id, user=request.user)
    
    if request.method == 'POST':
        form = PendienteForm(request.POST, instance=pendiente)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pendiente actualizado exitosamente.')
            return redirect('pendientes_ids_titles')
    else:
        form = PendienteForm(instance=pendiente)
    
    context = {
        'form': form,
        'pendiente': pendiente,
        'titulo': 'Editar Pendiente'
    }
    return render(request, 'core/editar_pendiente.html', context)

@login_required
def marcar_resuelto(request, pendiente_id):
    """Vista para marcar un pendiente como resuelto"""
    pendiente = get_object_or_404(Pendiente, id=pendiente_id, user=request.user)
    pendiente.resuelto = not pendiente.resuelto
    pendiente.save()
    
    estado = "resuelto" if pendiente.resuelto else "pendiente"
    messages.success(request, f'Pendiente marcado como {estado}.')
    
    return redirect('pendientes_ids_titles')

@login_required
def crear_pendiente(request):
    if request.method == 'POST':
        form = PendienteForm(request.POST)
        if form.is_valid():
            pendiente = form.save(commit=False)
            pendiente.user = request.user  
            pendiente.save()
            return redirect('index')  
    else:
        form = PendienteForm()

    return render(request, 'core/crear_pendiente.html', {
        'form': form,
        'titulo': 'Crear Nuevo Pendiente'
    })

@login_required
def eliminar_pendiente(request, pendiente_id):
    pendiente = get_object_or_404(Pendiente, id=pendiente_id, user=request.user)
    pendiente.delete()
    return redirect('pendientes_ids_titles') 