from django import forms
from .models import Anken


class AnkenForm(forms.ModelForm):
    class Meta:
        model = Anken
        fields = ('pub_date',
                'ankenmei',
                'iraibusho',
                'iraisha',
                'nouki',
                'mitumorikousu',
                'naiyou',
                'genjouchi', 
                'kitaikouka', 
                'tantousha',  
                'koumoku', 
                'joutai', 
                'jissekikousu',
                )