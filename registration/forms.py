from django import forms


class UserRegister(forms.Form):
    user_name = forms.CharField(required="true", label="user name", max_length=20)
    first_name = forms.CharField(required="true", label="first name", max_length=20)
    last_name = forms.CharField(required="true", label="last name", max_length=20)
    email = forms.EmailField(required="true", label="email id")
    password = forms.CharField(widget=forms.PasswordInput)
    address = forms.CharField(required="true", label="address")
    contact = forms.IntegerField(required="true")
    widgets = {
        'password': forms.PasswordInput(),
    }

class CompanyRegister(forms.Form):
    company_name=forms.CharField(required="true",label="user name" ,max_length=20 )
    first_name=forms.CharField(required="true",label="first name",max_length=20)
    last_name=forms.CharField(required="true",label="last name", max_length=20)
    email=forms.EmailField(required="true",label="email id")
    password=forms.CharField(widget=forms.PasswordInput)
    address=forms.CharField(required="true",label="address")
    contact=forms.IntegerField(required="true")
    widgets = {
            'password': forms.PasswordInput(),
    }

class JobSubmit(forms.Form):
    genre = forms.CharField(required="true", label="Genre", max_length=20)
    details = forms.CharField(required="true", label="Job Details", max_length=200000)
    pay = forms.CharField(required="true", label="Pay Offered", max_length=50)
    dead_line = forms.IntegerField(required="true")


class ApplicationSubmit(forms.Form):
    application = forms.CharField(required="true", label="Job Application", max_length=200000)
    pay_expected = forms.CharField(required="true", label="Pay Expected", max_length=50)

class logInUser(forms.Form):
    user_name = forms.CharField(required="true", label="User name", max_length=20)
    password = forms.CharField(widget=forms.PasswordInput())
    widgets = {
         'password': forms.PasswordInput(),
     }
class logInCompany(forms.Form):
    company_name = forms.CharField(required="true", label="Company name", max_length=20)
    password = forms.CharField(widget=forms.PasswordInput())
    widgets = {
         'password': forms.PasswordInput(),
     }

class SearchJob(forms.Form):
    search=forms.CharField(required="true", label="search",max_length=100)
    pay_Salary=forms.CharField(required="true",max_length=50)
