from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import Waifu, Comment, Rate
from django.forms import ModelForm, TextInput, NumberInput, CharField, PasswordInput, HiddenInput


class AddWaifuForm(ModelForm):
    class Meta:
        model = Waifu
        fields = ['name', 'description', 'waifu_pic']

class AddCommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['value']

class AddRateForm(ModelForm):
    class Meta:
        model = Rate
        fields = ['value']
