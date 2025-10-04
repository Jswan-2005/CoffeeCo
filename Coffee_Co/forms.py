from django import forms
from .models import CoffeeType, CoffeeRecipeEntry

class CoffeeTypeForm(forms.ModelForm):
    class Meta:
        model = CoffeeType
        fields = ['text']
        labels = {'text': ''}

class CoffeeRecipeEntryForm(forms.ModelForm):
    rating = forms.ChoiceField(
        choices=[(i, str(i)) for i in range(1, 6)],
        widget=forms.RadioSelect,
        required=True,
    )

    class Meta:
        model = CoffeeRecipeEntry
        fields = ['text', 'rating']
        labels = {'text': 'Entry:'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}

