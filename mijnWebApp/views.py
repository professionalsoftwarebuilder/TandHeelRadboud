from django.shortcuts import render, HttpResponse
from .models import *

def index(request):
    deArtikelen = Artikel.objects.all()
    context = {'deArtikelen': deArtikelen}
    return render(request, 'mijnWebApp/index.html', context)

def product(request, prod_id):
    deArtikel = Artikel.objects.get(id=prod_id)
    context = {'deArtikel': deArtikel}
    return render(request, 'mijnWebApp/product.html', context)

def contact(request):
    return render(request, 'mijnWebApp/contact.html', {})
