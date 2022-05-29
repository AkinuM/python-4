import logging

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, ListView
from django.http import HttpResponse
from django.contrib.auth.mixins import UserPassesTestMixin

from .forms import AddWaifuForm, AddCommentForm, AddRateForm
from .models import Waifu, Rate, Comment

logger = logging.getLogger('django')

class WaifusView(View):
    def get(self, request):
        waifus = Waifu.objects.order_by('-rating')
        return render(request, 'main/home.html', {'waifus': waifus})


class AddWaifuView(UserPassesTestMixin, CreateView):
    model = Waifu
    form_class = AddWaifuForm
    success_url = '/'
    template_name = 'main/add_waifu.html'

    def test_func(self):
        return self.request.user.is_staff


class WaifuDetailView(CreateView):
    model = Rate
    template_name = 'main/waifu_details.html'
    form_class = AddRateForm

    def get_success_url(self):
        return self.request.path

    def form_valid(self, form):
        obj = form.save(commit=False)
        rate = Rate.objects.filter(waifu_id=self.kwargs['pk'], user__username=self.request.user.username)
        if len(rate):
            rate.delete()
        obj.value = self.request.POST.get('value')
        obj.user = self.request.user
        obj.waifu = Waifu.objects.get(pk=self.kwargs['pk'])
        obj.save()
        ratings = Rate.objects.filter(waifu_id=self.kwargs['pk'])
        value = 0.0
        count = len(ratings)
        for rate in ratings:
            value += rate.value
        if count:
            obj.waifu.rating = value / count
        obj.waifu.save()
        return super(WaifuDetailView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        rating = super(WaifuDetailView, self).get_context_data(**kwargs)
        rating['rating'] = Waifu.objects.get(pk=self.kwargs['pk']).rating
        rate = Rate.objects.filter(waifu_id=self.kwargs['pk'], user__username=self.request.user.username)
        if len(rate):
            rating['rate'] = rate[0].value
        else:
            rating['rate'] = 0
        rating['comments'] = Comment.objects.filter(waifu_id=self.kwargs['pk'])
        rating['waifu'] = Waifu.objects.get(pk=self.kwargs['pk'])
        return rating


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


class AddCommentView(UserPassesTestMixin, CreateView):
    model = Comment
    form_class = AddCommentForm
    template_name = 'main/add_comment.html'

    def test_func(self):
        return self.request.user.is_authenticated

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.waifu = Waifu.objects.get(pk=self.kwargs['pk'])
        obj.save()
        return super(AddCommentView, self).form_valid(form)

class RegisterView(CreateView):
    form_class = UserCreationForm
    success_url = '/'
    template_name = 'main/register.html'