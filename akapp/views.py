from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView
from .forms import AnkenForm
from django.urls import reverse_lazy
from .models import Anken
from django.utils import timezone

class IndexView(TemplateView):
    template_name = 'akapp/index.html'


class AnkenCreateView(CreateView):
    template_name = 'akapp/anken_create.html'
    form_class = AnkenForm
    success_url = reverse_lazy('akapp:anken_create_complete')


class AnkenCreateCompleteView(TemplateView):
    template_name = 'akapp/anken_create_complete.html'


class AnkenListView(ListView):
    template_name = 'akapp/anken_list.html'
    model = Anken


class AnkenDetailView(DetailView):
    template_name = 'akapp/anken_detail.html'
    model = Anken


class AnkenUpdateView(UpdateView):
    template_name = 'akapp/anken_update.html'
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
    success_url = reverse_lazy('akapp:anken_list')

    def form_valid(self, form):
        anken = form.save(commit=False)
        anken.pub_date = timezone.now()
        anken.save()
        return super().form_valid(form)


class AnkenDeleteView(DeleteView):
    template_name = 'akapp/anken_delete.html'
    model = Anken
    success_url = reverse_lazy('akapp:anken_list')