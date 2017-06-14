from django import forms
from amsite.models import Info, Revw, Mark, Descript



class InfoForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = ('__all__')

class RevwForm(forms.ModelForm):
    class Meta:
        model = Revw
        fields = ('__all__')

class MarkForm(forms.ModelForm):
    class Meta:
        model = Mark
        fields = ('__all__')

class DescForm(forms.ModelForm):
    class Meta:
        model = Descript
        fields = ('__all__')
