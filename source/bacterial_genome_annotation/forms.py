#from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import User

class UserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email',)


class UserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email',)

class SearchForm(forms.Form):
    bacterial_name = forms.CharField(max_length=100, required=False)
    nucleic_or_peptidic = forms.ChoiceField(choices = ((True,'Nucleic'),(False,'Peptidic')), required=False)
    sequence = forms.CharField(max_length = 100, min_length=3, required=False)
    gene_name = forms.CharField(max_length = 100, required=False)
    transcript_name = forms.CharField(max_length = 100, required=False)
    description = forms.CharField(max_length = 100, required=False)

class AnnotForm(forms.Form):
    id = forms.CharField(max_length=50, required=False) # The same than the sequence but with '.X' with X a number to allow multipple annotation.
    gene = forms.CharField(max_length=10, required=False)
    gene_biotype = forms.CharField(max_length=50, required=False)
    transcript_biotype = forms.CharField(max_length=50, required=False)
    gene_symbol = forms.CharField(max_length=10, required=False)
    description = forms.CharField(max_length=200, required=False)
    transcript = forms.CharField(max_length=200,required=False)
    isValidate = forms.BooleanField(required=False)
    
class CommentForm(forms.Form):
    comment = forms.CharField(max_length=500)

#default=''    
    
    
    