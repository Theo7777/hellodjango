from writer.models import UserEmail
from django import forms
from django.forms import ModelForm


class EmailForm(ModelForm):
	email = forms.EmailField()

	class Meta:
		model = UserEmail



