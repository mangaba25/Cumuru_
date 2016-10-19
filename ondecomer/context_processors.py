# coding=utf-8

from .models import CategoryOndeComer


def categoriaondecomer(request):
    return {
        'categoriaondecomer': CategoryOndeComer.objects.all()
    }