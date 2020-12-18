from django import forms
from .models import requirement, testcase
#import der Choices damit die überall verwendbar sind
from .choices import *


class RequirementForm(forms.Form):
    #Felder die verändert werden können
    req_form_name = forms.CharField(widget=forms.Textarea(attrs={"rows": 2, "cols": 80}))
    req_form_beschreibung = forms.CharField(widget=forms.Textarea(attrs={"rows": 2, "cols": 80}))
    req_form_kommentar = forms.CharField(widget=forms.Textarea(attrs={"rows": 2, "cols": 80}))

    form_category = forms.ChoiceField(choices=KATEGORIEN)

class TestCaseForm(forms.Form):
    #Felder die verändert werden können
    testc_form_name = forms.CharField(widget=forms.Textarea(attrs={"rows": 2, "cols": 80}))
    testc_form_beschreibung = forms.CharField(widget=forms.Textarea(attrs={"rows": 5, "cols": 80}))
    testc_form_kommentar = forms.CharField(widget=forms.Textarea(attrs={"rows": 5, "cols": 80}))
    testc_form_vorbedingung = forms.CharField(widget=forms.Textarea(attrs={"rows": 5, "cols": 80}))

    testc_form_fk_requirement = forms.ModelMultipleChoiceField(queryset=None ,widget=forms.CheckboxSelectMultiple)

    def __init__(self, *args, **kwargs):
        reqs = kwargs.pop('reqs')
        super(TestCaseForm, self).__init__(*args, **kwargs)
        self.fields["testc_form_fk_requirement"].queryset = reqs

class TestCase_Schritt_Form(forms.Form):
    #Felder die verändert werden können
    schritt_form_schritt = forms.CharField(widget=forms.Textarea(attrs={"rows": 5, "cols": 60}))
    schritt_form_erwartetesergebnis = forms.CharField(widget=forms.Textarea(attrs={"rows": 5, "cols": 60}))

class TestCase_Schritt_Form2(forms.Form):
    #Felder die verändert werden können
    schritt_form_tatsaechlichesergebnis = forms.CharField(widget=forms.Textarea(attrs={"rows": 5, "cols": 40}))
    schritt_ergebnis = forms.CharField(label='ergebnis', widget=forms.RadioSelect(choices=RUN_STATUS))


class TestRunForm(forms.Form):
    # Felder die verändert werden können
    testr_form_name = forms.CharField(widget=forms.Textarea(attrs={"rows": 2, "cols": 80}))
    testr_form_beschreibung = forms.CharField(widget=forms.Textarea(attrs={"rows": 2, "cols": 80}))
    testr_form_kommentar = forms.CharField(widget=forms.Textarea(attrs={"rows": 2, "cols": 80}))

    testr_form_status = forms.ChoiceField(choices=RUN_STATUS)

    testr_form_fk_testcase = forms.ModelChoiceField(queryset=None ,widget=forms.RadioSelect)

    def __init__(self, *args, **kwargs):
        tecs = kwargs.pop('tecs')
        super(TestRunForm, self).__init__(*args, **kwargs)
        self.fields["testr_form_fk_testcase"].queryset = tecs


class GroupForm(forms.Form):
    # Felder die verändert werden können
    group_form_group = forms.ChoiceField(choices=GRUPPEN)

