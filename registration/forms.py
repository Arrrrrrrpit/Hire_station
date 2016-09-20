from django import forms


class UserRegister(forms.Form):
    user_name = forms.CharField(required="true", label="user name", max_length=20,
                                widget=forms.TextInput(attrs={'placeholder': 'User Name'}))
    first_name = forms.CharField(required="true", label="first name", max_length=20,
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(required="true", label="last name", max_length=20,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    email = forms.EmailField(required="true", label="email id",widget=forms.TextInput(attrs={'placeholder': 'Email' }))
    password = forms.CharField(widget=forms.PasswordInput)
    address = forms.CharField(required="true", label="address",widget=forms.TextInput(attrs={'placeholder': 'Address' }))
    contact = forms.IntegerField(required="true",widget=forms.TextInput(attrs={'placeholder': 'Contact' }))
    widgets = {
        'password': forms.PasswordInput(),
    }


class CompanyRegister(forms.Form):
    company_name = forms.CharField(required="true", label="Company name", max_length=20,
                                    widget=forms.TextInput(attrs={'placeholder': 'Company Name' })
                                    )
    first_name = forms.CharField(required="true", label="first name", max_length=20,
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(required="true", label="last name", max_length=20,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    email = forms.EmailField(required="true", label="email id",
                             widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput)
    address = forms.CharField(required="true", label="address",widget=forms.TextInput(attrs={'placeholder': 'Address' }))
    contact = forms.IntegerField(required="true",widget=forms.TextInput(attrs={'placeholder': 'Contact' }))
    widgets = {
        'password': forms.PasswordInput(),

    }



class JobSubmit(forms.Form):
    genre = forms.CharField(required="true", label="Genre", max_length=20,
                            widget=forms.TextInput(attrs={'placeholder': 'Genre'}))
    details = forms.CharField(required="true", label="Job Details", max_length=200000,
                              widget=forms.TextInput(attrs={'placeholder': 'Details'}))
    pay = forms.IntegerField(required="true",widget=forms.TextInput(attrs={'placeholder': 'Pay' }))
    dead_line = forms.CharField(required="true",label="Dead Line",max_length=20,
                                widget=forms.TextInput(attrs={'placeholder': 'Deadline'}))


class ApplicationSubmit(forms.Form):
    application = forms.CharField(required="true", label="Job Application", max_length=200000)
    pay_expected = forms.IntegerField(required="true")


class ProfileAdd(forms.Form):
    profile_img = forms.ImageField()
    website_linked = forms.URLField(label="Link your Website")
    user_introduction = forms.CharField(label="Self Introduction")


class LogInUser(forms.Form):
    user_name = forms.CharField(required="true", label="User name", max_length=20,
                                widget=forms.TextInput(attrs={'placeholder': 'User Name'}))
    password = forms.CharField(widget=forms.PasswordInput())
    widgets = {
        'password': forms.PasswordInput(),
    }


class LogInCompany(forms.Form):
    company_name = forms.CharField(required="true", label="Company name", max_length=20,
                                   widget=forms.TextInput(attrs={'placeholder': 'Company Name'}))
    password = forms.CharField(widget=forms.PasswordInput())
    widgets = {
        'password': forms.PasswordInput(),
    }


class SearchJob(forms.Form):
    search = forms.CharField(required="true", label="search", max_length=100)
    pay_Salary = forms.IntegerField(required="true")
