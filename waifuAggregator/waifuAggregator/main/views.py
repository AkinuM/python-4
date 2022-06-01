import asyncio
import logging

from asgiref.sync import sync_to_async
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


@sync_to_async()
def get_ordered_waifus(str):
    return Waifu.objects.order_by(str)

@sync_to_async()
def get_rate_waifu_user(waifu_id, user_username):
    return Rate.objects.filter(waifu_id=waifu_id, user__username=user_username)

@sync_to_async()
def get_waifu(waifu_id):
    return Waifu.objects.get(pk=waifu_id)

@sync_to_async()
def get_rate_waifu(waifu_id):
    return Rate.objects.filter(waifu_id=waifu_id)

@sync_to_async()
def get_comment_waifu(waifu_id):
    return Comment.objects.filter(waifu_id=waifu_id)


class WaifusView(View):
    def get(self, request):
        waifus = asyncio.run(get_ordered_waifus('-rating'))
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
        rate = asyncio.run(get_rate_waifu_user(self.kwargs['pk'], self.request.user.username))
        if len(rate):
            rate.delete()
        obj.value = self.request.POST.get('value')
        obj.user = self.request.user
        obj.waifu = asyncio.run(get_waifu(self.kwargs['pk']))
        obj.save()
        ratings = asyncio.run(get_rate_waifu(self.kwargs['pk']))
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
        rating['rating'] = asyncio.run(get_waifu(self.kwargs['pk'])).rating
        rate = asyncio.run(get_rate_waifu_user(self.kwargs['pk'], self.request.user.username))
        if len(rate):
            rating['rate'] = rate[0].value
        else:
            rating['rate'] = 0
        rating['comments'] = asyncio.run(get_comment_waifu(self.kwargs['pk']))
        rating['waifu'] = asyncio.run(get_waifu(self.kwargs['pk']))
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
        obj.waifu = asyncio.run(get_waifu(self.kwargs['pk']))
        obj.save()
        return super(AddCommentView, self).form_valid(form)


class RegisterView(CreateView):
    form_class = UserCreationForm
    success_url = '/'
    template_name = 'main/register.html'
