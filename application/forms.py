from django import forms
from application.models import Cliente

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'