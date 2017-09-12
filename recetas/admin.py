# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.

from django import forms
from django.contrib import admin
from django.core.files.images import get_image_dimensions
from recetas.models import Receta, Ingrediente, Implemento, Paso, Version, MeGusta, Compartido, Unidad


class RecetaForm(forms.ModelForm):

    class Meta:
        model = Receta
        fields = '__all__'

    def clean_imagen(self):
        imagen = self.cleaned_data.get("imagen")

        if not imagen:
            # raise forms.ValidationError("No image!")
            pass
        else:
            w, h = get_image_dimensions(imagen)
            if w != 386:
                raise forms.ValidationError(
                    "La imagen que intenta subir tiene %i pixeles de ancho. El tamaño permitido es 386px" % w)
            if h != 249:
                raise forms.ValidationError(
                    "La imagen que intenta subir tiene %h pixeles de alto. El tamaño permitido es 249px" % h)
        return imagen


class RecetaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'region', 'porciones', 'tiempo_preparacion')
    search_fields = ('nombre', 'region')
    list_filter = ('region', 'porciones', 'tiempo_preparacion')
    filter_horizontal = ('ingredientes', 'implementos', 'pasos')
    ordering = ('nombre',)
    form = RecetaForm


class IngredienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nombre2', 'cantidad', 'unidad')
    search_fields = ('nombre', 'nombre2')
    list_filter = ('unidad',)
    # filter_horizontal = ('unidad', 'cantidad')
    ordering = ('nombre',)


class UnidadAdmin(admin.ModelAdmin):
    list_display = ('unidad',)
    ordering = ('unidad',)


class ImplepementoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)
    ordering = ('nombre',)


class PasoAdmin(admin.ModelAdmin):
    list_display = ('referencia', 'orden',  'paso')
    search_fields = ('referencia', 'paso')
    list_filter = ('referencia',)


class VersionAdmin(admin.ModelAdmin):
    list_display = ('version', 'fecha')


class MeGustaAdmin(admin.ModelAdmin):

    def receta_id(self, obj):
        return obj.receta.id

    list_display = ('receta_id', 'receta', 'fecha', 'usuario_id')


class CompartidoAdmin(admin.ModelAdmin):

    def receta_id(self, obj):
        return obj.receta.id

    list_display = ('receta_id', 'receta', 'fecha', 'usuario_id')

admin.site.register(Receta, RecetaAdmin)
admin.site.register(Ingrediente, IngredienteAdmin)
admin.site.register(Unidad, UnidadAdmin)
admin.site.register(Implemento, ImplepementoAdmin)
admin.site.register(Paso, PasoAdmin)
admin.site.register(Version, VersionAdmin)
admin.site.register(MeGusta, MeGustaAdmin)
admin.site.register(Compartido, CompartidoAdmin)
