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
        '''widgets = {
            'pub_date': forms.DateInput(attrs={'class': 'form-control'}),
            'ankenmei': forms.TextInput(attrs={'class': 'form-control'}),
            'iraibusho': forms.TextInput(attrs={'class': 'form-control'}),
            'iraisha': forms.TextInput(attrs={'class': 'form-control'}),
            'nouki': forms.DateInput(attrs={'class': 'form-control'}),
            'mitumorikousu': forms.TextInput(attrs={'class': 'form-control'}),
            'naiyou': forms.TextInput(attrs={'class': 'form-control'}),
            'genjouchi': forms.TextInput(attrs={'class': 'form-control'}),
            'kitaikouka': forms.TextInput(attrs={'class': 'form-control'}),
            'tantousha': forms.TextInput(attrs={'class': 'form-control'}),
            'koumoku': forms.TextInput(attrs={'class': 'form-control'}),
            'joutai': forms.TextInput(attrs={'class': 'form-control'}),
            'jissekikousu': forms.TextInput(attrs={'class': 'form-control'}),
            
        }
        '''
        
    
    