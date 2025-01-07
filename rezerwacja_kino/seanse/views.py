from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Seans, Rezerwacja
from django.shortcuts import get_object_or_404, redirect

class SeanseListView(ListView):
    model = Seans
    template_name = "lista_seansow.html"

class SeanseDetailView(DetailView):
    model = Seans
    template_name = "szczegoly_seansow.html"

class RezerwacjaDetailView(DetailView):
    model = Rezerwacja
    template_name = "szczegoly_rezerwacji.html"
    
def create_reservation(request, pk, bilety):
    if request.action =="POST" and request.user.is_authenticated:
        seans = get_object_or_404(Seans, pk=pk)
        if seans.liczba_wolnych_miejsc() >= bilety:
            rezerwacja = Rezerwacja.object.create(
                user=request.user,
                seans=seans,
                liczba_biletow=bilety
            )
            return redirect(f"rezerwacje/{rezerwacja.id}")
        return redirect(f"seans/{seans.id}")
