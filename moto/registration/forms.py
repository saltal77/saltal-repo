from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):

    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control',
                                                       'placeholder': 'Ваш Login'}), required=True)
    first_name = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control',
                                                        'placeholder': 'Ваше Имя'}), required=False)
    email = forms.EmailField(label='Почта', widget=forms.TextInput(attrs={'class': 'form-control',
                                                        'placeholder': 'mail@site.com'}), required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']
        # fields = '__all__'

class UserChangeForm(forms.ModelForm):

    """
    Форма для обновления данных пользователей. Нужна только для того, чтобы не
    видеть постоянных ошибок "Не заполнено поле password" при обновлении данных
    пользователя.
    """
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']
