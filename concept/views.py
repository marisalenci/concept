from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

from .models import Phrase, Concept, Token

def home(request):
    context = {
        'first_name': 'Marisa',
        'last_name': 'Lenci',
        'concepts': Concept.objects.all(),
        'phrases': Phrase.objects.all(),
    }
    return render(request, 'home.html', context)


class TokenList(ListView):
    model = Token

class TokenDetail(DetailView):
    model = Token

class CreateToken(CreateView):
    model = Token
    fields = ('color', 'is_primary')
    success_url = reverse_lazy('token-list')

class UpdateToken(UpdateView):
    model = Token
    fields = ('concept',)
    success_url = reverse_lazy('token-list')
