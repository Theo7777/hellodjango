# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render

def pageload(request):
	return render(request, 'home.html') 
	
	
