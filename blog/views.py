from django.shortcuts import render
from django.utils import timezone   # pridane
from .models import Post            # na pridanie modelu z models.py

# Create your views here.
def post_list(request):    # vytvorili sme premennu post na odovzdavanie QuerySet ktora je aj jeho menom
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
                            # Posledný parameter, {} je miesto na ktoré môžeme dať nejaké veci
                            # ktoré môže použiť šablóna. Potrebujeme im dať mená (zatiaľ sa
                            # budeme držať 'posts'). :) Malo by to vyzerať takto: {'posts': posts}.
                            # Všimni si, že časť pred : je reťazec: potrebuješ ju obaliť do úvodzoviek:"