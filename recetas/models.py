# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


def path_and_rename(path):
    def wrapper(instance, filename):
        ext = filename.split('.')[-1]
        # get filename
        if instance.pk:
            filename = '{}.{}'.format(instance.pk, ext)
        else:
            # set filename as random string
            filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(path, filename)
    return wrapper


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Version(models.Model):
    version = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Versiones"

    def __unicode__(self):
        return (str(self.version)+". "+str(self.fecha))


class Unidad(models.Model):
    unidad = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Unidades"

    def __unicode__(self):
        return self.unidad


class Ingrediente(models.Model):
    nombre = models.CharField(
        max_length=200, help_text='Nombre como es conocido comúnmente el ingrediente',)
    nombre2 = models.CharField(
        max_length=200, help_text='Otro nombre con el que pueda ser reconocido el alimento', blank=True, null=True, verbose_name='otros nombres')
    cantidad = models.CharField(max_length=5)
    unidad = models.ForeignKey(
        Unidad, related_name='ingredientes', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Ingredientes"

    def __unicode__(self):
        return "%s (%s %s)" % (self.nombre, self.cantidad, self.unidad.unidad)


class Implemento(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(
        blank=True, null=True, verbose_name='Descripción')

    class Meta:
        verbose_name_plural = "Implementos"

    def __unicode__(self):
        return self.nombre


class Paso(models.Model):
    orden = models.PositiveSmallIntegerField(
        help_text='Orden del paso según la receta')
    referencia = models.CharField(
        max_length=40, help_text='Referencia para ubicar el paso facilmente',)
    # paso = RichTextField(help_text='Pasos para realizar la receta', verbose_name="Preparación")
    paso = models.TextField(help_text='Pasos para realizar la receta',
                            verbose_name="Preparación")

    class Meta:
        verbose_name_plural = " Pasos"

    def __unicode__(self):
        return "(%s) %d. %s" % (self.referencia, self.orden, self.paso)


class Receta (models.Model):
    nombre = models.CharField(max_length=200, help_text='Nombre de la receta')
    imagen = models.ImageField(blank=True, null=True, upload_to='recetas',
                               help_text='Las imagenes deben tener un tamaño de 386x249 pixeles')
    # pais = models.CharField(max_length=45)
    region = models.CharField(
        max_length=45, help_text='Región de donde es la receta', verbose_name='Región')
    porciones = models.PositiveSmallIntegerField(
        help_text='La cantidad de porciones finales de la receta.')
    tiempo_preparacion = models.CharField(
        max_length=45, help_text='Duración de preparacion de la receta en minutos', verbose_name='Tiempo de preparación')
    ingredientes = models.ManyToManyField(Ingrediente)

    pasos = models.ManyToManyField(Paso,
                                   help_text='Pasos para realizar la receta', verbose_name="Pasos de la receta")
    implementos = models.ManyToManyField(
        Implemento, help_text='Implementos utilisados en la elaboración de la receta')
    sugerencia = models.TextField(
        blank=True, null=True, help_text='Sugerencia en la elaboración de la receta para los lectores')
    owner = models.ForeignKey('auth.User', related_name='recetas',
                              blank=True, null=True, on_delete=models.CASCADE)

    is_active = models.BooleanField(default=False, verbose_name='Activo',
                                    help_text='Determina si la receta es visible en la app o no')

    class Meta:
        verbose_name_plural = "  Recetas"

    def __unicode__(self):
        return self.nombre


class Compartido (models.Model):
    receta = models.ForeignKey(
        Receta, related_name='compartidos', on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    usuario_id = models.IntegerField(
        help_text='Id de usuario que interactua')

    class Meta:
        verbose_name_plural = "Compartidos"
        ordering = ['receta', 'usuario_id']

    def __unicode__(self):
        return unicode(self.receta)


class MeGusta (models.Model):
    receta = models.ForeignKey(
        Receta, related_name='me_gustas', on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    usuario_id = models.IntegerField(
        help_text='Id de usuario que interactua')

    class Meta:
        verbose_name_plural = "Me gustas"
        unique_together = ('receta', 'usuario_id')
        ordering = ['receta', 'usuario_id']

    def __unicode__(self):
        return unicode(self.receta)


@receiver(post_save, sender=Receta, dispatch_uid="update_version")
@receiver(post_save, sender=Compartido, dispatch_uid="update_version")
@receiver(post_save, sender=MeGusta, dispatch_uid="update_version")
def update_version(sender, instance=None, **kwargs):
    Version.objects.create()
