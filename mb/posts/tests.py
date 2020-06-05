from django.test import TestCase
from .models import Message
# Create your tests here.
class MessageModelTest(TestCase):
	def setUp(self):
		Message.objects.create(message="this is a test")
	def test_message_conten(self):
		x=Message.objects.get(id=1)
		expected=f'{x.message}'
		self.assertEqual('this is a test',expected)

class ChatviewViewTest(TestCase):
	def setUp(self):
		Message.objects.create(message='this is a test')


	def check_home_page_code(self):
		response=self.client.get('/home')
		self.assertEqual(response.status_code,200)

