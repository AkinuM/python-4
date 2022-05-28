from django.shortcuts import render
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView
from django.http import HttpResponse
from django.contrib.auth.mixins import UserPassesTestMixin

from .forms import AddWaifuForm, AddCommentForm
from .models import Waifu, Rate, Comment


def home(request):
    waifus = Waifu.objects.all()
    return render(request, 'main/home.html', {'waifus': waifus})

class AddWaifuView(UserPassesTestMixin, CreateView):
    model = Waifu
    form_class = AddWaifuForm
    success_url = '/'
    template_name = 'main/add_waifu.html'

    def test_func(self):
        return self.request.user.is_staff

class WaifuDetailView(DetailView, CreateView):
    model = Waifu
    template_name = 'main/waifu_details.html'
    context_object_name = 'waifu'
    form_class = AddCommentForm

    def get_context_data(self, **kwargs):
        rating = super(WaifuDetailView, self).get_context_data(**kwargs)
        ratings = Rate.objects.filter(waifu=self.object)
        value = 0.0
        count = len(ratings)
        for rate in ratings:
            value += rate.value
        if count:
            rating['rating'] = value/count
        else:
            rating['rating'] = 0
        ratings = Rate.objects.filter(waifu=self.object)
        rating['isRate'] = len(ratings)
        rating['comments'] = Comment.objects.filter(waifu=self.object)
        return rating

class AddRateView(CreateView):
    model = Rate
    success_url = '{% url "waifu-detail" model.waifu.id %}'
    template_name = 'main/waifu_details.html'

class WaifuDeleteView(UserPassesTestMixin, DeleteView):
    model = Waifu
    success_url = '/'
    template_name = 'main/waifu_delete.html'

    def test_func(self):
        return self.request.user.is_staff

class WaifuEditView(UserPassesTestMixin, UpdateView):
    model = Waifu
    form_class = AddWaifuForm
    template_name = 'main/add_waifu.html'

    def test_func(self):
        return self.request.user.is_staff
