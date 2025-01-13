from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Seans, Rezerwacja
from django.shortcuts import get_object_or_404, redirect
from django.db.models import Sum, F

class SeanseListView(ListView):
    model = Seans
    template_name = "lista_seansow.html"

    def get_queryset(self):
        qs = Seans.objects.annotate(zarezerwowane_miejsca=Sum("rezerwacje__liczba_biletow")).filter(sala__liczba_miejsc__gt=F("zarezerwowane_miejsca"))
        return qs
    

class SeanseDetailView(DetailView):
    model = Seans
    template_name = "szczegoly_seansow.html"

class RezerwacjaDetailView(DetailView):
    model = Rezerwacja
    template_name = "szczegoly_rezerwacji.html"
    
def create_reservation(request, pk):
    if request.method == "POST" and request.user.is_authenticated:
        seans = get_object_or_404(Seans, pk=pk)
        bilety = int(request.POST.get('bilety'))
        if seans.liczba_wolnych_miejsc() >= bilety:
            rezerwacja = Rezerwacja.objects.create(
                user=request.user,
                seans=seans,
                liczba_biletow=bilety
            )
            return redirect(f"/seanse/rezerwacje/{rezerwacja.id}")
        return redirect(f"seans/{seans.id}")
