# coding=utf-8

from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import OndeFicar, CategoryOndeFicar, ImageOndeficar

# Create your views here.
class ListarListView(generic.ListView):
	model = OndeFicar
	template_name = 'ondeficar/lista-ondeficar.html'
	context_object_name = 'object_list'
	paginate_by = 3
	
listar = ListarListView.as_view()

class CategoryListView(generic.ListView):
	template_name = 'ondeficar/descricao-ondeficar.html'
	context_object_name = 'object_list'
	paginate_by = 3

	def get_queryset(self):
		return OndeFicar.objects.filter(category__slug=self.kwargs['slug'])

	def get_context_data(self, **kwargs):
		context = super(CategoryListView, self).get_context_data(**kwargs)
		context['current_category'] = get_object_or_404(CategoryOndeFicar, slug=self.kwargs['slug'])
		context['capa'] = ImageOndeficar.objects.all()
		return context

category = CategoryListView.as_view()	

# def listar(request):
# 	queryset = OndeFicar.objects.all()
# 	context = {
# 		"object_list": queryset
# 	}
# 	return render(request, 'ondeficar/lista-ondeficar.html', context)

# def category(request, slug):
# 	capa = ImageOndeficar.objects.all()
# 	category = CategoryOndeFicar.objects.get(slug=slug)
# 	context = {
# 		'current_category': category,
# 		'object_list': OndeFicar.objects.filter(category=category),
# 		"capa": capa
# 	}
# 	return render(request, 'ondeficar/descricao-ondeficar.html', context)

def ondeficar(request, slug):
	ondeficar = OndeFicar.objects.get(slug=slug)
	context = {
		'ondeficar': ondeficar
	}
	return render(request, 'ondeficar/slide-ondeficar.html', context)

	capa = ImageOndecomer.objects.all()
