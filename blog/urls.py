from django.urls import path  # nie url ale pri Django ver. 4+ path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),  # r'^$' nahradene '', post_list je home page
        # po ^ (začiatku) bude nasledovať $ (koniec)
        # Tento vzor povie Djangu, že views.post_list je to správne miesto,
        # kam treba ísť, ak niekto vstúpi na stránku cez adresu 'http://127.0.0.1:8000/'
        # name='post_list' je názov URL, ktorý sa použije na identifikáciu zobrazenia
    path(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
        # odkazanie Django na view nazvaný post_detail, ktorý zobrazí celý príspevok blogu
    path(r'^post/new/$', views.post_new, name='post_new'),
        # odkazanie Django na view nazvaný post_new, ktorý zobrazí formular blogu
    path(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
        # pridanie nasledujuceho riadku kvoli upravam post-ov
    path('drafts/', views.post_draft_list, name='post_draft_list'),
        # pridane za ucelom vytvorenia zoznamu docasnych (draft) post-ov
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),
        # pridane za ucelom publish - publikovania
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
        # pridane za ucelom Delete - zmazania
]
