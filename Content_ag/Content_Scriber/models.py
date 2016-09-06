from django.db import models

""" Defining the Job publishing form field """



class job_details(models.Model):
        
	details = models.CharField(max_length=100000)
        pay = models.CharField(max_length=50)
        deadline = models.DateTimeField('Date to complete the project till')
	pub_date = models.DateTimeField('date published')

""" defining the job Application submit field """

class job_application(models.Model):
	question = models.ForeignKey(job_details, on_delete=models.CASCADE)
	Application_text = models.CharField(max_length=100000)
	status = models.BooleanField(default=10)


