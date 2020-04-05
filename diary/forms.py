from django import forms
from django.utils import timezone
from django.contrib.auth.forms import AuthenticationForm
from .models import Writer, Record, MAX_TITLE_LEN, MAX_CONTENT_LEN


class WriterLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            # field.widget.attrs['placeholder'] = field.label


class WriteForm(forms.Form):
    content = forms.CharField(
        max_length=MAX_CONTENT_LEN,
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )
    title = forms.CharField(max_length=MAX_TITLE_LEN,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    date = forms.DateField(initial=timezone.now(),
                           widget=forms.DateInput(attrs={'class': 'form-control'}))
    status = forms.ChoiceField(choices=Record.STATES,
                               widget=forms.RadioSelect(
                                   attrs={'class': 'form-check-input'})
                               )

    def record(self, writer, content, title, date, status):
        rc = Record(writer=writer, content=content,
                    title=title, date=date, status=status)
        rc.save()
        return rc
