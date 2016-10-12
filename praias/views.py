# coding=utf-8


from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Praia, CategoryPraia, ImagePraia


class ListarListView(generic.ListView):
	model = Praia
	template_name = 'praias/lista-praias.html'
	context_object_name = 'object_list'
	paginate_by = 8

	def get_context_data(self, **kwargs):
		context = super(ListarListView, self).get_context_data(**kwargs)
		context['capa'] = ImagePraia.objects.all()
		return context

	
listar = ListarListView.as_view()

class CategoryListView(generic.ListView):
	template_name = 'praias/descricao-praias.html'
	context_object_name = 'object_list'
	paginate_by = 8

	def get_queryset(self):
		return Praia.objects.filter(category__slug=self.kwargs['slug'])

	def get_context_data(self, **kwargs):
		context = super(CategoryListView, self).get_context_data(**kwargs)
		context['current_category'] = get_object_or_404(CategoryPraia, slug=self.kwargs['slug'])
		return context

category = CategoryListView.as_view()






# def listar(request):
# 	capa = ImagePraia.objects.all()
# 	queryset = Praia.objects.all()
# 	context = {
# 		"object_list": queryset,
# 		"capa": capa
# 	}
# 	return render(request, 'praias/lista-praias.html', context)

# def category(request, slug):
# 	category = CategoryPraia.objects.get(slug=slug)
# 	context = {
# 		'current_category': category,
# 		'object_list': Praia.objects.filter(category=category),
# 	}
# 	return render(request, 'praias/descricao-praias.html', context)

def praia(request, slug):
	praia = Praia.objects.get(slug=slug)
	context = {
		'praia': praia
	}
	return render(request, 'praias/slide-praias.html', context)



	