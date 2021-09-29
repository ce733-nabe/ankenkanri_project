from django import forms
from .models import Anken, Shuho
import bootstrap_datepicker_plus as datetimepicker
#from django_summernote.widgets import SummernoteWidget

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
                'updated_at',
                'image'
                )
        widgets = {
            'nouki': datetimepicker.DateTimePickerInput(
                format='%Y-%m-%d %H:%M:%S',
                options={
                    'locale': 'ja',
                    'dayViewHeaderFormat': 'YYYY年 MMMM',
                }
            ),
            #'naiyou': SummernoteWidget(),
        }
                
        
class ShuhoForm(forms.ModelForm):
    class Meta:
        model = Shuho
        fields = ('anken',
                'pub_date',
                'naiyou',
                'categori',
                'updated_at',
                )
        #exclude = ('anken',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['naiyou'].initial = '<p>＜実施内容＞</p><p>＜結果・問題点＞</p><p>＜次回予定＞</p><p>＜添付先＞<p/>'
        
        #self.fields['anken'].queryset = Anken.objects.filter(id=1)
        
        
        
    
    