from home.models import *
from django import forms

TITLE_CHOICES = (
    ("Professor", "Professor"),
    ("Associate Professor", "Associate Professor"),
    ("Assistant Professor", "Assistant Professor"),
)

YES_OR_NO = (
    (True, 'Yes'),
    (False, 'No')
)

PUBLICATION_CHOICES = (
    ("Journal Paper", "Journal Paper"),
    ("Conference - Workshop Paper", "Conference - Workshop Paper"),
    ("Book", "Book"),
    ("Book Chapter", "Book Chapter"),
    ("Patent", "Patent"),
    ("Research Poster", "Research Poster"),
)

PROGRAM_TYPES_CHOICES = (('Graduate', 'Graduate'),
                         ('Undergraduate', 'Undergraduate'))


class FacultyMemberForm(forms.ModelForm):
    title = forms.ChoiceField(choices=TITLE_CHOICES)
    chair = forms.ChoiceField(choices=YES_OR_NO,
                              label='Are you department chair?',
                              initial=False)

    vice_chair = forms.ChoiceField(choices=YES_OR_NO,
                                   label='Are you department vice chair?',
                                   initial=False)

    leave = forms.ChoiceField(choices=YES_OR_NO,
                              label='Are you on leave?',
                              initial=False)

    visit = forms.ChoiceField(choices=YES_OR_NO,
                              label='Are you a visiting faculty member?',
                              initial=False)

    class Meta:
        model = FacultyMember
        exclude = []


class PublicationForm(forms.ModelForm):
    type_of = forms.ChoiceField(choices=PUBLICATION_CHOICES,
                                label='Type',
                                initial=False)

    class Meta:
        model = Publication
        exclude = ['fetched_from_google_scholar', 'fetched_from_DBLP']


class ProgramForm(forms.ModelForm):
    type_of = forms.ChoiceField(choices=PROGRAM_TYPES_CHOICES,
                                label='Type',
                                initial=False)

    class Meta:
        model = Program
        exclude = []
