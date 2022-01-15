from django.contrib import admin
from .models import Post    # importovanie namodelovaneho modelu blogu postu z minulej kapitoly

# Register your models here.

admin.site.register(Post)   # kvoli pridavaniu, editovanie a mazanie namodelovanych postov

                            # viac o admine https://docs.djangoproject.com/en/1.11/ref/contrib/admin/