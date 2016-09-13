from django.db import models

""" Defining the Job seeker registration form field """


class JobSeeker(models.Model):
    user_name = models.CharField(primary_key=True, max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email_id = models.EmailField()
    password = models.CharField(max_length=20)
    address = models.TextField()
    contact_number = models.IntegerField(default=0)


""" defining the job provider registration field """


class JobProvider(models.Model):
    company_name = models.CharField(primary_key=True, max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email_id = models.EmailField()
    password = models.CharField(max_length=20)
    address = models.TextField()
    contact_number = models.IntegerField(default=0)


""" defining the job request submit field """


class JobDetails(models.Model):
    company_name = models.CharField(max_length=20)
    job_id = models.AutoField(primary_key=True, default=1)
    genre = models.CharField(max_length=20)
    details = models.CharField(max_length=100000)
    pay = models.CharField(max_length=50)
    deadline = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')


""" defining the job Application submit field """


class JobApplication(models.Model):
    user_name= models.CharField(default="guest",max_length=20)
    job_id = models.AutoField(primary_key=True,default=1)
    application_text = models.CharField(max_length=100000)
    pay_expected = models.CharField(max_length=200)
    status = models.BooleanField(default=10)
