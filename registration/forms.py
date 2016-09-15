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
    company_name = forms.CharField(required="true", label="Company name", max_length=20)
    first_name = forms.CharField(required="true", label="first name", max_length=20)
    last_name = forms.CharField(required="true", label="last name", max_length=20)
    email = forms.EmailField(required="true", label="email id")
    password = forms.CharField(widget=forms.PasswordInput)
    address = forms.CharField(required="true", label="address")
    contact = forms.IntegerField(required="true")
    widgets = {
        'password': forms.PasswordInput(),
    }


class JobSubmit(forms.Form):
    genre = forms.CharField(required="true", label="Genre", max_length=20)
    details = forms.CharField(required="true", label="Job Details", max_length=200000)
    pay = forms.IntegerField(required="true")
    dead_line = forms.CharField(required="true",label="Dead Line",max_length=20)


class ApplicationSubmit(forms.Form):
    application = forms.CharField(required="true", label="Job Application", max_length=200000)
    pay_expected = forms.IntegerField(required="true")


class ProfileAdd(forms.Form):
    profile_img = forms.ImageField()
    website_linked = forms.CharField(label="Link your Website")
    user_introduction = forms.CharField(label="Self Introduction")


class LogInUser(forms.Form):
    user_name = forms.CharField(required="true", label="User name", max_length=20)
    password = forms.CharField(widget=forms.PasswordInput())
    widgets = {
        'password': forms.PasswordInput(),
    }


class LogInCompany(forms.Form):
    company_name = forms.CharField(required="true", label="Company name", max_length=20)
    password = forms.CharField(widget=forms.PasswordInput())
    widgets = {
        'password': forms.PasswordInput(),
    }


class SearchJob(forms.Form):
    search = forms.CharField(required="true", label="search", max_length=100)
    pay_Salary = forms.IntegerField(required="true")
