from django import forms
#import der Choices damit die überall verwendbar sind
from .choices import *


class RequirementForm(forms.Form):
    form_category = forms.ChoiceField(choices=KATEGORIEN)

