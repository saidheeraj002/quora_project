from django import forms
from .models import Users, Question, Answer

class LoginForm(forms.Form):
    username = forms.CharField(
        label='Username',
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data['username']
        password = cleaned_data.get('password')

        user_details = Users.objects.filter(username=username)
        if user_details:
            if username == user_details[0].username and password == user_details[0].password:
                return cleaned_data
            else:
                raise forms.ValidationError("Invalid username or password.")
        else:
            raise forms.ValidationError("Invalid username or password.")


class RegistrationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=150)
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    confirm_password = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        if Users.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already taken.")
        return username

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError(
                "The passwords you entered do not match."
            )
        return cleaned_data

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Question Title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Optional: Add more details'}),
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Write your answer...'}),
        }
        labels = {
            'content': '' # Hide the default label if desired
        }

