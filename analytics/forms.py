from django import forms


class MultipleFileInput(forms.FileInput):
    allow_multiple_selected = True


class UserReport(forms.Form):
    file = forms.FileField(
        label="Отчет:",
        widget=MultipleFileInput(attrs={'multiple': True}),
        required=False
    )
