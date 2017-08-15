from django.contrib import admin

# Register your models here.

from django import forms
from django.contrib import admin
from django.core.files.images import get_image_dimensions
from recetas.models import Receta, Ingrediente, Implemento, Paso


class RecetaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'region', 'porciones', 'tiempo_preparacion')
    search_fields = ('nombre', 'region')
    list_filter = ('region', 'porciones', 'tiempo_preparacion')
    filter_horizontal = ('ingredientes', 'implementos', 'pasos')
    ordering = ('nombre',)


class IngredienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nombre2', 'cantidad', 'unidad')
    search_fields = ('nombre', 'nombre2')
    list_filter = ('unidad',)
    #filter_horizontal = ('unidad', 'cantidad')
    ordering = ('nombre',)


class ImplepementoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)
    ordering = ('nombre',)


class PasoAdmin(admin.ModelAdmin):
    list_display = ('referencia', 'orden',  'paso')
    search_fields = ('referencia', 'paso')
    list_filter = ('referencia',)


admin.site.register(Receta, RecetaAdmin)
admin.site.register(Ingrediente, IngredienteAdmin)
admin.site.register(Implemento, ImplepementoAdmin)
admin.site.register(Paso, PasoAdmin)
