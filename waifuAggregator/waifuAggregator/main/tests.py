import json

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Waifu, Rate, Comment


class BlogTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )

        self.waifu = Waifu.objects.create(
            name='Stass',
            description='Nice body bro',
            waifu_pic='/main/static/main/img/peg.jpg'
        )

        self.rate = Rate.objects.create(
            value=4,
            user=self.user,
            waifu=self.waifu
        )

        self.comment = Comment.objects.create(
            value='Stass the best',
            user=self.user,
            waifu=self.waifu
        )

    def test_string_representation(self):
        self.assertEqual(str(self.waifu), self.waifu.name)
        self.assertEqual(str(self.comment), self.comment.user.username)
        self.assertEqual(str(self.rate), self.rate.value.__str__())

    def test_get_absolute_url(self):
        self.assertEqual(self.waifu.get_absolute_url(), f'/{self.waifu.id}')
        self.assertEqual(self.comment.get_absolute_url(), f'/{self.waifu.id}')
        self.assertEqual(self.rate.get_absolute_url(), f'/{self.waifu.id}')

    def test_content(self):
        self.assertEqual(f'{self.waifu.name}', 'Stass')
        self.assertEqual(f'{self.waifu.description}', 'Nice body bro')
        self.assertEqual(f'{self.waifu.waifu_pic}', '/main/static/main/img/peg.jpg')

        self.assertEqual(f'{self.comment.value}', 'Stass the best')
        self.assertEqual(self.comment.user, self.user)
        self.assertEqual(self.comment.waifu, self.waifu)

        self.assertEqual(self.rate.value, 4)
        self.assertEqual(self.rate.user, self.user)
        self.assertEqual(self.rate.waifu, self.waifu)

    def test_waifu_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/home.html')

    def test_waifu_detail_view(self):
        response = self.client.get(reverse('waifu-detail', args=f'{self.waifu.id}'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/waifu_details.html')

    def test_waifu_create_view(self):
        response = self.client.post(reverse('add-waifu'))
        self.assertEqual(response.status_code, 302)

    def test_waifu_update_view(self):
        response = self.client.post(reverse('waifu-edit', args='1'))
        self.assertEqual(response.status_code, 302)

    def test_waifu_delete_view(self):
        response = self.client.post('/accounts/login/', {'username': 'testuser', 'password': 'secret'})
        self.assertEqual(response.status_code, 302)
        response = self.client.post(reverse('waifu-delete', args=f'{self.waifu.id}'))
        self.assertEqual(response.status_code, 403)

    def test_comment_view(self):
        response = self.client.post(reverse('add-comment', args=f'{self.waifu.id}'))
        self.assertEqual(response.status_code, 302)

    def test_register_view(self):
        response = self.client.post(reverse('register'))
        self.assertEqual(response.status_code, 200)
