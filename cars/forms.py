from django import forms
from .models import Review
from django.forms import ModelForm

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        # fields = ['fName','lName', 'stars']
        fields = "__all__"

        labels = {
            'fName' : "First Name",
            'lName' : "Last Name"
        }

        error_messages = {
            'stars' : { 'min_value': "Min value is 1",'max_value':'Max value is 5'
            }
        }
# class ReviewForm(forms.Form):
#     fName = forms.CharField(label='First Name', max_length=100)
#     lName = forms.CharField(label='Last Name', max_length=100)
#     email = forms.EmailField(label='Email')
#     review = forms.CharField(label="Review", widget=forms.Textarea())
#     # review = forms.CharField(label="Review", widget=forms.Textarea(attrs={'class':'myForm'}))

