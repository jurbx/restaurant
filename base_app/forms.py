from django import forms
from .models import ModelFormRegistration


class FormRegistration(forms.ModelForm):
    name = forms.CharField(max_length=50,
                           widget=forms.TextInput(attrs={
                               "type": "text", "name": "name", "class": "form-control", "id": "name",
                               "placeholder": "Your Name", "data-rule": "minlen:4",
                               "data-msg": "Please enter at least 4 chars"
                           }))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        "type": "email", "class": "form-control", "name": "email", "id": "email", "placeholder": "Your Email",
        "data-rule": "email", "data-msg": "Please enter a valid email"
    }))
    phone = forms.CharField(max_length=15,
                            widget=forms.TextInput(attrs={
                                'type': "text", 'class': "form-control", 'name': "phone", 'id': "phone",
                                'placeholder': "Your Phone", 'data-rule': "minlen:4",
                                'data-msg': "Please enter at least 4 chars"
                            }))
    date = forms.DateField(widget=forms.TextInput(attrs={'type': "text", 'name': "date", 'class': "form-control",
                                                         'id': "date", 'placeholder': "Date", 'data-rule': "minlen:4",
                                                         'data-msg': "Please enter at least 4 chars"}),
                           input_formats=['%Y.%m.%d', '%Y-%m-%d', '%Y %m %d',
                                          '%d.%m.%Y', '%d-%m-%Y', '%d %m %Y'])

    time = forms.DateTimeField(widget=forms.TextInput(attrs={'type': "text", 'class': "form-control", 'name': "time",
                                                         'id': "time", 'placeholder': "Time", 'data-rule': "minlen:4",
                                                         'data-msg': "Please enter at least 4 chars"}),
                               input_formats=['%H:%M'])

    count_of_people = forms.IntegerField(widget=forms.TextInput(attrs={'type': "number", 'class': "form-control",
                                                                          'name': "people", 'id': "people",
                                                                          'placeholder': "# of people",
                                                                          'data-rule': "minlen:1",
                                                                          'data-msg': "Please enter at least 1 chars"}))

    message = forms.CharField(max_length=400,
                              widget=forms.Textarea(attrs={
                                'class': "form-control", 'name': "message", 'rows': "5", 'placeholder': "Message"
                              }))

    class Meta:
        model = ModelFormRegistration
        fields = ('name', 'email', 'phone', 'date', 'time', 'count_of_people', 'message')
