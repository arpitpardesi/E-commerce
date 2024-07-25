from django import forms

class ReviewForm(forms.Form):
    fName = forms.CharField(label='First Name', max_length=100)
    lName = forms.CharField(label='Last Name', max_length=100)
    email = forms.EmailField(label='Email')
    review = forms.CharField(label="Review")
