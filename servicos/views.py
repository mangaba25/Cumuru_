# coding=utf-8

from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Servico, CategoryServico, ImageServico


class ListarListView(generic.ListView):
	model = Servico
	template_name = 'servicos/lista-servicos.html'
	context_object_name = 'object_list'
	paginate_by = 3

	def get_context_data(self, **kwargs):
		context = super(ListarListView, self).get_context_data(**kwargs)
		context['capa'] = ImageServico.objects.all()
		return context

	
listar = ListarListView.as_view()

class CategoryListView(generic.ListView):
	template_name = 'servicos/descricao-servicos.html'
	context_object_name = 'object_list'
	paginate_by = 3

	def get_queryset(self):
		return Servico.objects.filter(category__slug=self.kwargs['slug'])

	def get_context_data(self, **kwargs):
		context = super(CategoryListView, self).get_context_data(**kwargs)
		context['current_category'] = get_object_or_404(CategoryServico, slug=self.kwargs['slug'])
		return context

category = CategoryListView.as_view()
# def listar(request):
# 	capa = ImageServico.objects.all()
# 	queryset = Servico.objects.all()
# 	context = {
# 		"object_list": queryset,
# 		"capa": capa
# 	}
# 	return render(request, 'servicos/lista-servicos.html', context)

# def category(request, slug):
# 	category = CategoryServico.objects.get(slug=slug)
# 	context = {
# 		'current_category': category,
# 		'object_list': Servico.objects.filter(category=category),
# 	}
# 	return render(request, 'servicos/descricao-servicos.html', context)

def servico(request, slug):
	servico = Servico.objects.get(slug=slug)
	context = {
		'servico': servico
	}
	return render(request, 'servicos/slide-servicos.html', context)

	