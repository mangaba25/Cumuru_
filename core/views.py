from django.shortcuts import render
<<<<<<< HEAD
from django.contrib.sitemaps import Sitemap
from home.models import Home, Aviso, Dica


=======
from home.models import Home, Aviso, Dica

>>>>>>> 372fb89680b88e5dd6fb36c75288ade693f18f8f
# Create your views here.
def index(request):
	home = Home.objects.all()
	dica = Dica.objects.all()
	aviso = Aviso.objects.all()
	context = {
		"home": home,
		"dica": dica,
		"aviso": aviso
	}
	return render(request, 'index.html', context)

def comochegar(request):
	return render(request, 'comochegar.html')
<<<<<<< HEAD
=======







>>>>>>> 372fb89680b88e5dd6fb36c75288ade693f18f8f
