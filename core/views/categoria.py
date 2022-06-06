from rest_framework.viewsets import ModelViewSet
from core.models import Categoria
from core.serializers import CategoriaSerializer
from django.core.cache import cache


class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer