from django.views.generic import TemplateView, CreateView
from .forms import AnkenForm
from django.urls import reverse_lazy

class IndexView(TemplateView):
    template_name = 'akapp/index.html'


class AnkenCreateView(CreateView):
    template_name = 'akapp/anken_create.html'
    form_class = AnkenForm
    success_url = reverse_lazy('akapp:anken_create_complete')


class AnkenCreateCompleteView(TemplateView):
    template_name = 'akapp/anken_create_complete.html'