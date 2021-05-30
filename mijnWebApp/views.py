from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import *
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.http import HttpResponseRedirect
from datetime import datetime, timezone, timedelta
from .forms import *
import pytz

def index(request):
    #deArtikelen = Artikel.objects.all()
    #context = {'deArtikelen': deArtikelen}
    return render(request, 'mijnWebApp/index.html', {})


def momenten(request, usr_id):
    theProfile = Profile.objects.get(pk=usr_id)
    PoetsMomenten = PoetsMoment.objects.filter(ptm_User_id=usr_id)
    context = {'PoetsMomenten': PoetsMomenten}
    return render(request, 'mijnWebApp/poetsmomenten_list.html', context)


def product(request, prod_id):
    #deArtikel = Artikel.objects.get(id=prod_id)
    #context = {'deArtikel': deArtikel}
    return render(request, 'mijnWebApp/product.html', {})

def contact(request):
    return render(request, 'mijnWebApp/contact.html', {})

class PoetsMomentCreateView(CreateView):
    form_class = PoetsMomentForm
    model = PoetsMoment
    #fields = [ 'ptm_Interval', 'ptm_Toothpaste', 'ptm_Activity', 'ptm_Notes']

    def get_initial(self):
        # Get record that was inserted before
        recBefore = PoetsMoment.objects.latest('ptm_Moment')
        # Get value from Datatime field
        timeBefore = getattr(recBefore, 'ptm_Moment')
        tz = pytz.timezone('Europe/Amsterdam')
        timeInterval = datetime.now(tz) - timeBefore
        print('timeintv', timeInterval)

        return {'ptm_Interval': timeInterval}


class PoetsMomentUpdateView(UpdateView):
    model = PoetsMoment
    fields = ['ptm_Interval', 'ptm_Toothpaste', 'ptm_Activity', 'ptm_Notes']


class PoetsMomentDeleteView(DeleteView):
    model = PoetsMoment

    def get_success_url(self):
        self.object = self.get_object()
        usr_id = self.object.ptm_User_id
        if usr_id:
            self.success_url = reverse_lazy('mijnApp:list_PoetsMomenten', kwargs={'usr_id': usr_id})
        else:
            # Ik moet ergens naar toe
            self.success_url = reverse_lazy('mijnApp:index')

        return self.success_url

    # I need to return the userid to list brushmoments by user
    def delete(self, request, *args, **kwargs):

        self.get_object().delete()
        return HttpResponseRedirect(self.get_success_url())

