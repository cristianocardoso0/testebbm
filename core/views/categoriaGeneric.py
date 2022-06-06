
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from core.models import Categoria
from core.serializers import CategoriaSerializer

# exemplo usando generics
class CategoriasListGeneric(ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaDetailGeneric(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
