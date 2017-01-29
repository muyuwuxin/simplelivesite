from django import forms


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2= forms.CharField(label='Confirm',widget=forms.PasswordInput)
    def pwd_validate(self,p1,p2):
        return p1==p2

class ChangepwdForm(forms.Form):
    username = forms.CharField()
    old_password = forms.CharField(widget=forms.PasswordInput)
    new_password= forms.CharField(label='New password',widget=forms.PasswordInput)
    new_password2= forms.CharField(label='Confirm',widget=forms.PasswordInput)

    def pwd_validate(self,p1,p2):
        return p1==p2


class ApplyForm(forms.Form):
    id_card = forms.CharField(max_length=30)
    title  = forms.CharField(max_length=30)
    describe =  forms.CharField(max_length=200)
