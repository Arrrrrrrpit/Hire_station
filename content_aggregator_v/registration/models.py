from django.db import models

""" Defining the Job seeker registration form field """


class job_seeker(models.Model):
    user_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email_id=models.EmailField()
    password=models.CharField(max_length=20)
    address=models.TextField()
    contact_number=models.IntegerField(default=0)

""" defining the job provider registration field """


class job_provider(models.Model):
    company_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email_id = models.EmailField()
    password = models.CharField(max_length=20)
    address = models.TextField()
    contact_number = models.IntegerField(default=0)

