from django import forms

class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=20, required=True)
    message = forms.CharField(widget=forms.Textarea)

class TeamForm(forms.Form):
    full_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=20, required=True)
    department = forms.CharField(max_length=100, required=True)
    bio = forms.CharField(required=True)