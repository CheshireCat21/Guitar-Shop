from register.models import User
from django.forms import ModelForm, TextInput


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name','nick_name','email','password','repeat_password']

        widgets = {
            "name": TextInput(attrs={
                "placeholder":"Write your name",
                "name": "name"
            }),
            "nick_name": TextInput(attrs={
                "placeholder": "Write your nick name",
                "name": "nick_name"
            }),
            "email": TextInput(attrs={
                "placeholder": "Enter Email",
                "name": "email"
            }),
            "password": TextInput(attrs={
                "placeholder": "at least 8 characters required!",
                "name": "psw",
                "type": "password"
            }),
            "repeat_password": TextInput(attrs={
                "placeholder": "Repeat Password",
                "name": "psw_repeat",
                "type": "password"
            })
        }