from django import forms

class job_S(forms.Form):
    user_N=forms.CharField(required="true",label="user name" ,max_length=20 )
    first_N=forms.CharField(required="true",label="first name",max_length=20)
    last_N=forms.CharField(required="true",label="last name", max_length=20)
    email=forms.EmailField(required="true",label="email id")
    password=forms.PasswordInput()
    address=forms.TextInput()
    contact=forms.IntegerField(required="true")

