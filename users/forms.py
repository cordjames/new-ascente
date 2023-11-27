from django import forms

class ProfileComparisonForm(forms.Form):
    favorite_color = forms.CharField(label='Favorite Color')
    pet_name = forms.CharField(label='Pet Name')
    maiden_name = forms.CharField(label='Maiden Name')