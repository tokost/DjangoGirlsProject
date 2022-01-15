                                    # vsetko az dole bolo pridane
# Create your models here.
from django.conf import settings    # from alebo import pridávajú časti z iných súborov
from django.db import models
from django.utils import timezone
                        # tento riadok definuje náš model (je to objekt class=trieda)
                            # Post je meno nášho modelu
class Post(models.Model):     # models.Model znamená, že Post je Django Model
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)   # definicia vlastnosti modelu vid.
    text = models.TextField()     # https://docs.djangoproject.com/en/1.11/ref/models/fields/#field-types
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):  # def znamená, že ide o funkciu/metódu a publish je názov metódy
        self.published_date = timezone.now()    # metódy často niečo vracajú (angl. return)
        self.save()
                        # def publish(self): a def __str__(self): sú odsadené vo vnútri našej triedy
    def __str__(self):  # keď zavoláme __str__(), dostaneme text (string) s názvom postu
        return self.title