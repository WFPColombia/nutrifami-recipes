# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from rest_framework import serializers
from recetas.models import Receta, Ingrediente, Implemento, Version
from django.contrib.auth.models import User


class IngredienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingrediente
        fields = ('nombre', 'nombre2', 'cantidad', 'unidad')


class ImplementoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Implemento
        fields = ('nombre', 'descripcion')


class VersionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Version
        fields = ('version', 'fecha')


class RecetaSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')
    ingredientes = IngredienteSerializer(many=True, read_only=True)
    implementos = ImplementoSerializer(many=True, read_only=True)

    class Meta:
        model = Receta
        fields = ('nombre', 'imagen', 'region', 'porciones', 'tiempo_preparacion',
                  'ingredientes', 'pasos', 'implementos', 'sugerencia', 'is_active', 'owner')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    proyectos = serializers.HyperlinkedRelatedField(
        many=True, view_name='receta-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'recetas')
