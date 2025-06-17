from django import forms
from django.forms import inlineformset_factory

from .models import Profile, PortfolioLink

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'profile_picture', 'bio', 'creative_fields']
        widgets = {
            'creative_fields': forms.CheckboxSelectMultiple(),
        }

PortfolioLinkFormSet = inlineformset_factory(
    Profile, PortfolioLink,
    fields=['link'],
    extra=3,
    max_num=3,
    can_delete=True
)