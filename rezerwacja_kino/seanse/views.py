from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Seans, Rezerwacja, Film
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Sum, F
from django.contrib.auth import login
from .forms import RejestracjaForm


class SeanseListView(ListView):
    model = Seans
    template_name = "lista_seansow.html"

    def get_queryset(self):
        
        seanse_z_wolnymi_miejscami = Seans.objects.annotate(zarezerwowane_miejsca=Sum("rezerwacje__liczba_biletow")).filter(sala__liczba_miejsc__gt=F("zarezerwowane_miejsca"))
        film_id = self.request.GET.get("film")
        if film_id:
            seanse_z_wolnymi_miejscami = seanse_z_wolnymi_miejscami.filter(film__id=film_id)

        qs = {
            "seanse": seanse_z_wolnymi_miejscami,
            "filmy": Film.objects.all()
        }
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

def rezerwacje_view(request):
    return render(request, "szczegoly_rezerwacji.html")

def lista_seansow_view(request):
    return render(request, "lista_seansow.html")

def rejestracja(request):
    if request.method == "POST":
        form = RejestracjaForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("lista-seansow")
    else:
        form = RejestracjaForm()
    return render(request, 'rejestracja.html', {'form': form})