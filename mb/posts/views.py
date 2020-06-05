from django.shortcuts import render
from django.views.generic import ListView
from .models import Message
# Create your views here.
class Chatview(ListView):
	model=Message
	template_name='home.html'
	context_object_name='all_posts_list'
	

