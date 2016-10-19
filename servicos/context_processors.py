# coding=utf-8

from .models import CategoryServico


def categoriaservico(request):
    return {
        'categoriaservico': CategoryServico.objects.all()
    }

   