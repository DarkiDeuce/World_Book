from django.shortcuts import render
from django.http import HttpResponse

def index(requst):
    return HttpResponse('Главная страница сайта Мир книг!')
