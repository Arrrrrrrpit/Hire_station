from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^jobseeker/$', views.get_user, name='registerUser'),
    url(r'^jobseeker/thanks/$', views.thanks, name='thanks'),
    url(r'^jobprovider/$', views.get_comapny, name='registerCompany'),
    url(r'^jobprovider/thanks/$', views.thanks, name='thanks'),
    url(r'^jobsubmit/$', views.get_job, name='Job Submit'),
    url(r'^jobapplication/$', views.get_application, name='Job Application'),
    url(r'^loginuser/$', views.login_user, name='loginUser'),
    url(r'^logincompany/$', views.login_Company, name='loginCompany'),
]
