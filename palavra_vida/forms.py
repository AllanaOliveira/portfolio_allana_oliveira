from django import forms

from palavra_vida.models import PalavraVida

class PalavraVidaForm(forms.ModelForm):

    class Meta:
        model = PalavraVida
        fields = {'nome', 'motivacao', 'avatar', 'localidade'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['nome'].error_messages={'required': 'Campo obrigatório!'}
        self.fields['nome'].widget.attrs.update({'class': 'form-control form-control-sm'})

        self.fields['motivacao'].error_messages = {'required': 'Campo obrigatório!'}
        self.fields['motivacao'].widget.attrs.update({'class': 'form-control form-control-sm'})

        self.fields['avatar'].error_messages = {'required': 'Campo obrigatório!'}

        self.fields['localidade'].error_messages = {'required': 'Campo obrigatório!'}
        self.fields['localidade'].widget.attrs.update({'class': 'form-control form-control-sm'})