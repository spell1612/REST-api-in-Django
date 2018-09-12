from django.utils.translation import gettext_lazy as _  #important!!

from django import forms
from .models import RandObject


class Prod(forms.ModelForm):
    class Meta:
        model=RandObject
        fields=['objectname','price']
        labels={
            'objectname': _('Name'),
        }
    # name=forms.CharField(label='Product Name', max_length=100,required=True )
    # price=forms.IntegerField(label='Price',required=True)
