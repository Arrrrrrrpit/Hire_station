from django.db import models


""" Defining the Job seeker registration form field """

class JobSeeker(models.Model):
    user_name = models.CharField(primary_key=True, max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email_id = models.EmailField()
    password = models.CharField(max_length=20)
    address = models.TextField()
    contact_number = models.IntegerField()


""" defining the job provider registration field """


class JobProvider(models.Model):
    company_name = models.CharField(primary_key=True, max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email_id = models.EmailField()
    password = models.CharField(max_length=20)
    address = models.TextField()
    contact_number = models.IntegerField()


""" defining the job request submit field """


class JobDetails(models.Model):
    company_name = models.CharField(primary_key=False, max_length=20)
    genre = models.CharField(max_length=20)
    details = models.CharField(primary_key=True,max_length=100000)
    pay = models.IntegerField(default=0)
    deadline = models.CharField(max_length=20)
    pub_date = models.DateTimeField('date published')


""" defining the job Application submit field """


class JobApplication(models.Model):
    company_name = models.CharField(default="guest",max_length=40)
    user_name= models.CharField(primary_key=True, default="guest",max_length=20)
    application_text = models.CharField(max_length=100000)
    pay_expected = models.IntegerField(default=0)
    status = models.BooleanField(default=10)


""" the user profile of any person """


class UserDetails(models.Model):
    user_name = models.CharField(primary_key=True, max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email_id = models.EmailField()
    address = models.TextField()
    contact_number = models.IntegerField(default=0)
    img = models.ImageField(null=True, blank=True, upload_to='media/', height_field="height_field",
                              width_field="width_field")
    website_linked = models.URLField()
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    user_introduction = models.CharField(max_length=20000, default= "")



