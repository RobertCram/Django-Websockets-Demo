from django import forms

class GalleryForm(forms.Form):
    '''GalleryForm'''
    number_of_images = forms.IntegerField(min_value=1)
    batch_number = forms.IntegerField(min_value=1)