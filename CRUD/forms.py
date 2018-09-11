from django import forms

class Prod(forms.Form):
    name=forms.CharField(label='Product Name', max_length=100,required=True )
    price=forms.IntegerField(label='Price',required=True)
