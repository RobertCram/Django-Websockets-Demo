"""
    Demo Views
"""
import time
import threading
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import PictureGenerator
from .forms import GalleryForm

BATCH_NUMBER = 0

def index(request):
    '''index'''

    if request.method == 'POST':
        form = GalleryForm(request.POST)
        if form.is_valid():
            number_of_images = form.cleaned_data['number_of_images']
            batch_number = form.cleaned_data['batch_number']
            thread = threading.Thread(target=thread_function, args=(number_of_images, batch_number))
            thread.start()
            return HttpResponseRedirect('/gallery/', )

    else:
        global BATCH_NUMBER
        BATCH_NUMBER += 1
        form = GalleryForm(initial = {'number_of_images': 30, 'batch_number': BATCH_NUMBER})

    return render(request, 'index.html', {'form': form})

def gallery(request):
    '''gallery'''
    return render(request, 'gallery.html')

def thread_function(images, batch_number):
    '''thread_function'''
    time.sleep(1) # give the socket time to connect
    generator = PictureGenerator()
    generator.generate(images, batch_number)
