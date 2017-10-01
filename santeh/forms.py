#-*- coding: utf-8 -*-

from __future__ import unicode_literals
from django import forms

from .models import *

class CommentForm(forms.ModelForm):

    author = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                            'placeholder': 'Ваше Имя'}), required=True)
    town = forms.CharField(label='Город', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                         'placeholder': 'Город'}),
                                 required=False)
    text = forms.CharField(label='Отзыв', widget=forms.Textarea(attrs={'class': 'form-control',
                                                                          'placeholder': 'Ваш отзыв'}),
                             required=True)

    class Meta:
        model = Comment
        fields = ('author', 'town', 'text',)


class OrderForm(forms.ModelForm):
    tlf = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                     'placeholder': 'Ваш телефон'}),required=False)
    
    class Meta:
        model = Order
        fields = '__all__'
        widgets = {
                  'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Ваше имя'}),
                  'email': forms.TextInput(attrs={'class': 'form-control',' placeholder':'Email'}),
                  'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Заявка или Сообщение'}),
                  }


#phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$',
#error_message = ("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
                                #'^\+\d{8,15}$'