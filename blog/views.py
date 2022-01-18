# from django.shortcuts import render - uz je importovane nizsie
from django.utils import timezone   # pridane
from .models import Post            # na pridanie modelu z models.py
from django.shortcuts import render, get_object_or_404
from .forms import PostForm         # importovanie nasej triedy PostForm t.j. nasho formulara
                                    # definovaneho vo forms.py
# Create your views here.
def post_list(request):    # vytvorili sme premennu post na odovzdavanie QuerySet ktora je aj jeho menom
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
                            # Posledný parameter, {} je miesto na ktoré môžeme dať nejaké veci
                            # ktoré môže použiť šablóna. Potrebujeme im dať mená (zatiaľ sa
                            # budeme držať 'posts'). :) Malo by to vyzerať takto: {'posts': posts}.
                            # Všimni si, že časť pred : je reťazec: potrebuješ ju obaliť do úvodzoviek:"

def post_detail(request, pk):   # pridanie nasho view pre post_detail
    post = get_object_or_404(Post, pk=pk)   # osetrenie situacie ak nie je ziaden Post s danym pk
                                # zobrazí sa stránka, Page Not Found 404, ktoru mozno upravit
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):  # Nový formulár Post vytvoríme tak, že sputíme PostForm() a prepošleme ho šablóne
    if request.method == "POST": # musíme ošetriť 2 prípady: 1, ak pristupujeme na stránku prvýkrát a chceme prázdny formulár,
                                 # a 2, keď sa vrátime na view s už predvyplnenými údajmi
        form = PostForm(request.POST) # pre 2 pripad uz mame z formulara v request.POST nejake udaje
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})