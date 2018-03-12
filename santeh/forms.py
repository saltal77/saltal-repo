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
    honey = forms.CharField(widget=forms.HiddenInput(attrs={'value': ''}), required=False)

    class Meta:
        model = Comment
        fields = ('author', 'town', 'text',)


class OrderForm(forms.ModelForm):

    tlf = forms.RegexField(regex=r'^\d{8,15}$',

                    widget=forms.TextInput(attrs={'class': 'form-control',
                                         'placeholder': 'Ваш телефон в формате 89998887766'}), required=False)
    honey = forms.CharField(widget=forms.HiddenInput(attrs={'value': ''}), required=False)
    # def __init__(self, *args, **kwargs):
    #     super(OrderForm, self).__init__(*args, **kwargs)
    #     self.fields['tlf'].error_messages = {'required': 'Не верно введен телефон, правилььный формат: 89098087766'}
    #
    class Meta:
        model = Order
        fields = '__all__'
        widgets = {
                  'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Ваше имя'}),
                  'email': forms.TextInput(attrs={'class': 'form-control',' placeholder':'Email'}),
                  'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Заявка или Сообщение'}),
                  }

