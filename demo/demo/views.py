"""
    Demo Views
"""
from django.shortcuts import render

def index(request):
    '''index'''
    return render(request, 'index.html')
