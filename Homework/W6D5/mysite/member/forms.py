from django import forms


class SignupForm(forms.Form):
    email = forms.EmailField(
        max_length=100,
        error_messages={
            'invalid': '이메일 형식이 아닙니다'
        },
        widget=forms.EmailInput(
            attrs={'class': 'form-control'}
        ),
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}
        ),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}
        ),
    )
    last_name = forms.CharField(
        max_length=20,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        ),
    )
    first_name = forms.CharField(
        max_length=20,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        ),
    )
    nickname = forms.CharField(
        max_length=20,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        ),
    )

