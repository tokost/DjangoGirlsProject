# from django.shortcuts import render - uz je importovane nizsie
from django.utils import timezone   # pridane
from .models import Post
# from .models import Post, Comment            na pridanie modelu z models.py a pridane Comment
from django.shortcuts import render, get_object_or_404, redirect
# from django.contrib.auth.decorators import login_required  zatial nepouzite
# from .forms import PostForm, CommentForm         importovanie nasej triedy PostForm t.j. nasho formulara a pridane CommentForm
from .forms import PostForm                                                    # definovaneho vo forms.py
#  from django.shortcuts import redirect  pridane vyssie aby sme sa pri pridavani dostali na zaciatok suboru

# Create your views here.
# creates the list of posts on the homepage
def post_list(request):    # vytvorili sme premennu post na odovzdavanie QuerySet ktora je aj jeho menom
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
                            # Posledný parameter, {} je miesto na ktoré môžeme dať nejaké veci
                            # ktoré môže použiť šablóna. Potrebujeme im dať mená (zatiaľ sa
                            # budeme držať 'posts'). :) Malo by to vyzerať takto: {'posts': posts}.
                            # Všimni si, že časť pred : je reťazec: potrebuješ ju obaliť do úvodzoviek:"

#what you see when you click on a post
def post_detail(request, pk):   # pridanie nasho view pre post_detail
    post = get_object_or_404(Post, pk=pk)   # osetrenie situacie ak nie je ziaden Post s danym pk
                                # zobrazí sa stránka, Page Not Found 404, ktoru mozno upravit
    return render(request, 'blog/post_detail.html', {'post': post})

#creating a new post-- login required, I don't think I need this view anymore
#since I have the one below it now!
# @login_required
# def post_new(request):
# 	form = PostForm()
# 	return render(request, 'blog/post_edit.html', {'form': form})

#  @login_required      decorator for securing the site, require login

def post_new(request):  # Nový formulár Post vytvoríme tak, že sputíme PostForm() a prepošleme ho šablóne
    if request.method == "POST": # musíme ošetriť 2 prípady: 1, ak pristupujeme na stránku prvýkrát a chceme prázdny formulár,
                                 # a 2, keď sa vrátime na view s už predvyplnenými údajmi
        form = PostForm(request.POST, request.FILES) # pre 2 pripad uz mame z formulara v request.POST nejake udaje a request.FILES pridane
        if form.is_valid():  # kontrola ci je formular v poriadku (všetky povinné polia sú vyplnené a nie sú zadané žiadne nesprávne hodnoty)
            post = form.save(commit=False)  # ak ano mozeme ho ulozit
            post.author = request.user  # este sa prida pole autor lebo toto nebolo v PostForm
#            post.published_date = timezone.now() vymazane kvoli draft-om z extensions
            post.save()  # uchová zmeny (pridanie autora) a máme vytvorený nový blog príspevok
            return redirect('post_detail', pk=post.pk) # prechod na stranku noveho prispevku
    else:                  # tento view vyžaduje premennú pk. Aby sme ju odovzdali do view, použijeme pk=post.pk
                           # post je novy blog a post_detail je názov view, kam chceme ísť
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

# edit a post that has already been written
# @login_required       pridane
def post_edit(request, pk):  # pridanie nasledujuceho bloku kvoli upravam post-ov
    post = get_object_or_404(Post, pk=pk) # odovzdávame navyše parameter pk z URL
                                          # pomocou get_object_or_404(Post, pk=pk)
                                          # získame tak Post model, ktorý chceme upravovať
    if request.method == "POST": # následne pri vytváraní formuláru odovzdáme tento post ako parameter instance,
        form= PostForm()   # pridane
#        form = PostForm(request.POST, instance=post)  # aj v prípade keď ukladáme formulár
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
#            post.published_date = timezone.now()  # vymazane kvoli draft-om z extensions
            post.save()         # aby nova posta bola ulozena ako draft
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)  # aj v prípade keď formulár upravujeme
    return render(request, 'blog/post_edit.html', {'form': form})
                        # nakolko znova použijeme šablónu post_edit.html

# list of posts that haven't been published yet (drafts)
#  @login_required     pridane
def post_draft_list(request):    # pridane za ucelom vytvorenia zoznamu docasnych(draft) post-ov
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})
        # do posts= vkladame iba nepublikovane post-y zoradene podla datumu

# manually publish a post
#   @login_required   pridane
def post_publish(request, pk):     # pridane za ucelom publikovania
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

# delete a post
#   @login_required   pridane
def post_remove(request, pk):       # pridane za ucelom zmazania
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

#  este nezabudovane
# def add_comment_to_post(request, pk):
#    post = get_object_or_404(Post, pk=pk)
#    if request.method == "POST":
#        form = CommentForm(request.POST)
#        if form.is_valid():
#            comment = form.save(commit=False)
#            comment.post = post
#            comment.save()
#            return redirect('post_detail', pk=post.pk)
#    else:
#        form = CommentForm()
#    return render(request, 'blog/add_comment_to_post.html', {'form': form})


# @login_required
# def comment_approve(request, pk):
#    comment = get_object_or_404(Comment, pk=pk)
#    comment.approve()
#    return redirect('post_detail', pk=comment.post.pk)

# @login_required
# def comment_remove(request, pk):
#   comment = get_object_or_404(Comment, pk=pk)
#    comment.delete()
#    return redirect('post_detail', pk=comment.post.pk)