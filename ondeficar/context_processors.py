# coding=utf-8

from .models import CategoryOndeFicar


def categoriaondeficar(request):
    return {
        'categoriaondeficar': CategoryOndeFicar.objects.all()
    }