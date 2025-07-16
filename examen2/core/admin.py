from django.contrib import admin
from .models import Pendiente

@admin.register(Pendiente)
class PendienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'resuelto', 'fecha_creacion', 'fecha_actualizacion')
    list_filter = ('resuelto', 'fecha_creacion', 'user')
    search_fields = ('title', 'description', 'user__username')
    list_editable = ('resuelto',)
    readonly_fields = ('fecha_creacion', 'fecha_actualizacion')
    
    fieldsets = (
        ('Información del Pendiente', {
            'fields': ('title', 'description', 'resuelto', 'user')
        }),
        ('Fechas', {
            'fields': ('fecha_creacion', 'fecha_actualizacion'),
            'classes': ('collapse',)
        }),
    )
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('user')