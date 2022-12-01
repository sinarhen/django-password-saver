from django import forms
from django.forms import ValidationError

INT_CHOICES = zip(range(1, 55), range(1, 55))


class PasswordSettingForm(forms.Form):
    digits = forms.BooleanField(required=False)
    special_symbols = forms.BooleanField(required=False)
    letters = forms.BooleanField(required=False)
    length = forms.TypedChoiceField(choices=INT_CHOICES, coerce=int)

    def clean(self):
        cleaned_data = self.cleaned_data
        if cleaned_data['digits'] or cleaned_data['special_symbols'] or cleaned_data['letters']:
            return cleaned_data
        raise ValidationError('You must pick at least one option to generate the password')
