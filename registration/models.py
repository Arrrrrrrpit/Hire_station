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
    company_name = models.CharField(default="guest", max_length=40)
    details = models.CharField(default="guest", max_length=10000)
    user_name= models.CharField( default="guest", max_length=20)
    application_text = models.CharField(primary_key=True, max_length=100000)
    email_user = models.EmailField(default="kunal716338@gmail.com")
    pay_expected = models.IntegerField(default=0)
    status = models.BooleanField(default=False)

""" Table containing job details and person selected for job"""
class JobsCompleted(models.Model):
    company_name = models.CharField(default="guest",max_length=40)
    user_name = models.CharField(default="guest", max_length=20)
    pay_given = models.IntegerField(default=0)

""" the user profile of any person """


class UserDetails(models.Model):
    user_name = models.CharField(primary_key=True, max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email_id = models.EmailField()
    address = models.TextField()
    contact_number = models.IntegerField(default=0)
    img = models.ImageField(null=True, blank=True, upload_to='media/', height_field="height_field",
                              width_field="width_field",default='media/default.png')
    website_linked = models.URLField(default="No Website Linked")
    height_field = models.IntegerField(null=True,default=100)
    width_field = models.IntegerField(null=True,default=100)
    user_introduction = models.CharField(max_length=20000, default= "No Introduction Added")



