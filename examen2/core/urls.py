from django.urls import path
from . import views

urlpatterns = [
    # Vista principal
    path('', views.index, name='index'),
    
    # Las 7 vistas del ToDO
    path('pendientes/ids/', views.pendientes_ids, name='pendientes_ids'),
    path('pendientes/ids-titles/', views.pendientes_ids_titles, name='pendientes_ids_titles'),
    path('pendientes/sin-resolver/', views.pendientes_sin_resolver, name='pendientes_sin_resolver'),
    path('pendientes/resueltos/', views.pendientes_resueltos, name='pendientes_resueltos'),
    path('pendientes/ids-users/', views.pendientes_ids_users, name='pendientes_ids_users'),
    path('pendientes/resueltos-users/', views.pendientes_resueltos_users, name='pendientes_resueltos_users'),
    path('pendientes/sin-resolver-users/', views.pendientes_sin_resolver_users, name='pendientes_sin_resolver_users'),
    
    

    # Vistas de CRUD
    path('crear/', views.crear_pendiente, name='crear_pendiente'),
    path('pendientes/editar/<int:pendiente_id>/', views.editar_pendiente, name='editar_pendiente'),
    path('pendientes/marcar-resuelto/<int:pendiente_id>/', views.marcar_resuelto, name='marcar_resuelto'),
    path('eliminar/<int:pendiente_id>/', views.eliminar_pendiente, name='eliminar_pendiente'),
]