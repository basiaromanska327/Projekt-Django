from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Seans

class SeanseListView(ListView):
    model = Seans
    template_name = "lista_seansow.html"

class SeanseDetailView(DetailView):
    model = Seans
    template_name = "szczegoly_seansow.html"
    


