from django import forms    # naimportovanie Django formulárov

from .models import Post    # naimportovanie nasho Post modelu

class PostForm(forms.ModelForm): # PostForm je nazov nasho formulara
                                # a Djangu tymto povieme ze je tento
                                # formular je ModelForm a forms umozni aby
                                # s nim Django mohol carovat
    class Meta:         # triedou Meta, Djangu povieme, ktorý model by mal byť použitý
        model = Post    #  na vytvorenie tohto formulára (model = Post)
        fields = ('title', 'text',) # Djangu povieme, ktoré polia budú v našom formulári.
                                    # V tomto scenári, chceme aby boli zobrazené iba title (nadpis) a text - author
                        # ty a dátum vytvorenia created_date by mali byť automaticky nastavene pri vytvorení postu