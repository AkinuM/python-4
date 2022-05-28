from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import Waifu, Comment
from django.forms import ModelForm, TextInput, NumberInput, CharField, PasswordInput

class AddWaifuForm(ModelForm):
    class Meta:
        model = Waifu
        fields = ['name', 'description', 'waifu_pic']

class AddCommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['value']
