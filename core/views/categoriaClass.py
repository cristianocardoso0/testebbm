from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from core.models import Categoria
import json

#exemplo basico usando json
@method_decorator(csrf_exempt, name='dispatch')
class CategoriaView(View):
    def get(self, request, id=None):
        if id:
            qs = Categoria.objects.get(id=id)
            data = {}
            data['id'] = qs.id
            data['nome'] = qs.nome
            return JsonResponse(data)
        else:
            data = list(Categoria.objects.values())
            formatted_data = json.dumps(data, ensure_ascii=False)
            return HttpResponse(formatted_data, content_type='application/json')
    
    def post(self, request):
        json_data = json.loads(request.body)
        nova_categoria = Categoria.objects.create(**json_data)
        data = {'id': nova_categoria.id, 'nome': nova_categoria.nome}
        return JsonResponse(data)

    def patch(self, request, id):
        json_data = json.loads(request.body)
        qs = Categoria.objects.get(id=id)
        qs.nome = json_data['nome']
        qs.save()
        data = {}
        data['id'] = qs.id
        data['nome'] = qs.nome
        return JsonResponse(data)
    
    def delete(self, request, id):
        qs = Categoria.objects.get(id=id)
        qs.delete()
        data = {'mensagem': 'Categoria excluida com sucesso'}
        return JsonResponse(data)