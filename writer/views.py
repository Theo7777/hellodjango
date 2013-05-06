# Create your views here.
from django.shortcuts import render
from writer.models import UserEmail
from writer.forms import EmailForm
from django.http import HttpResponseRedirect, HttpResponse

def EmailInput(request):
	if request.method == 'POST':
		form = EmailForm(request.POST)
		if form.is_valid():
			email = form['email']
			new_email = UserEmail(email = email)
			new_email.save()
			return render(request, 'success.html', {'email':email})
		else:
			return render(request, 'index.html')
	form = EmailForm()
	return render (request, 'index.html', {'form':form})


