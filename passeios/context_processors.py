# coding=utf-8

from .models import CategoryPasseio


def categoriapasseio(request):
    return {
        'categoriapasseio': CategoryPasseio.objects.all()
    }