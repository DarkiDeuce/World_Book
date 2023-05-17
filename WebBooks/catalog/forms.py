from django import forms
from datetime import date
from django.forms import ModelForm
from .models import Book
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class AuthorsForm(forms.Form):
    first_name = forms.CharField(label='Имя автора')
    last_name = forms.CharField(label='Фамилия автора')
    date_of_birth = forms.DateField(label='Дата рождения',
                                    initial=format(date.today()),
                                    widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    date_of_death = forms.DateField(label='Дата смерти',
                                    initial=format(date.today()),
                                    widget=forms.widgets.DateInput(attrs={'type': 'date'}))

class BookModelForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'genre', 'language', 'author', 'summary', 'isbn']

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(label='Ваше имя')
    last_name = forms.CharField(label='Ваша фамилия')

    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')