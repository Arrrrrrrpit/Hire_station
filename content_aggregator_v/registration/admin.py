from django.contrib import admin
from .models import job_seeker,job_provider


admin.site.register(job_seeker)
admin.site.register(job_provider)