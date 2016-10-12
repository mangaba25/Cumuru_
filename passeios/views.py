# coding=utf-8

from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Passeio, CategoryPasseio, ImagePasseio

# Create your views here.
class ListarListView(generic.ListView):
	model = Passeio
	template_name = 'passeios/lista-passeio.html'
	context_object_name = 'object_list'
	paginate_by = 3
	
listar = ListarListView.as_view()

class CategoryListView(generic.ListView):
	template_name = 'passeios/descricao-passeio.html'
	context_object_name = 'object_list'
	paginate_by = 3

	def get_queryset(self):
		return Passeio.objects.filter(category__slug=self.kwargs['slug'])

	def get_context_data(self, **kwargs):
		context = super(CategoryListView, self).get_context_data(**kwargs)
		context['current_category'] = get_object_or_404(CategoryPasseio, slug=self.kwargs['slug'])
		context['capa'] = ImagePasseio.objects.all()
		return context

category = CategoryListView.as_view()
# def listar(request):
# 	queryset = Passeio.objects.all()
# 	context = {
# 		"object_list": queryset
# 	}
# 	return render(request, 'passeios/lista-passeio.html', context)

# def category(request, slug):
# 	capa = ImagePasseio.objects.all()
# 	category = CategoryPasseio.objects.get(slug=slug)
# 	context = {
# 		'current_category': category,
# 		'object_list': Passeio.objects.filter(category=category),
# 		"capa": capa
# 	}
# 	return render(request, 'passeios/descricao-passeio.html', context)

def passeio(request, slug):
	passeio = Passeio.objects.get(slug=slug)
	context = {
		'passeio': passeio
	}
	return render(request, 'passeios/slide-passeio.html', context)


	


	