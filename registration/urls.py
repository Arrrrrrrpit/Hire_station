from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^jobseeker/$', views.get_name, name='register'),
    url(r'^jobseeker/thanks/$', views.thanks, name='thanks'),
    url(r'^jobsubmit/$', views.get_job, name='Job Submit'),
    url(r'^jobapplication/$', views.get_application, name='Job Application')
]
