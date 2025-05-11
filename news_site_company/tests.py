from django.test import TestCase
from django.contrib.auth.models import User
from .models import News, Comment
from django.urls import reverse

class NewsTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.staff_user = User.objects.create_user(username='staffuser', password='staffpassword', is_staff=True)
        self.news = News.objects.create(title='Test News', content='Test Content', author='testuser')

    def test_news_creation(self):
        self.assertEqual(News.objects.count(), 1)
        self.assertEqual(self.news.title, 'Test News')

    def test_news_editing(self):
        self.news.title = 'Edited News'
        self.news.save()
        self.assertEqual(News.objects.get(pk=self.news.pk).title, 'Edited News')

    def test_news_deletion(self):
        self.news.delete()
        self.assertEqual(News.objects.count(), 0)

    def test_staff_access_to_create_news(self):
        self.client.login(username='staffuser', password='staffpassword')
        url = reverse('news_create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_non_staff_access_to_create_news(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('news_create')
        response = self.client.get(url)
        self.assertIn(response.status_code, [302, 403])

    def test_comment_creation(self):
        self.client.login(username='testuser', password='testpassword')
        Comment.objects.create(news=self.news, user=self.user, text='Test Comment')
        self.assertEqual(Comment.objects.count(), 1)
        self.assertEqual(Comment.objects.first().text, 'Test Comment')