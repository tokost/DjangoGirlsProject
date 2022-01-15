from django.urls import path  # nie url ale pri Django ver. 4+ path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),  # r'^$' nahradene ''
]   # po ^ (začiatku) bude nasledovať $ (koniec)
    # Tento vzor povie Djangu, že views.post_list je to správne miesto,
    # kam treba ísť, ak niekto vstúpi na stránku cez adresu 'http://127.0.0.1:8000/'
    # name='post_list' je názov URL, ktorý sa použije na identifikáciu zobrazenia