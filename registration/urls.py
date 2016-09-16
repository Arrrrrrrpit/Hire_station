from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^jobseeker/$', views.get_user, name='registerUser'),
    url(r'^jobseeker/thanks/$', views.thanks, name='thanks'),
    url(r'^jobprovider/$', views.get_comapny, name='registerCompany'),
    url(r'^jobprovider/thanks/$', views.thanks, name='thanks'),
    url(r'^jobsubmit/$', views.get_job, name='Job Submit'),
    url(r'^jobapplication/$', views.get_application, name='Job Application'),
    url(r'^userprofile/edit/$', views.edit_profile_user, name='Profile Edit'),
    url(r'^companyprofile/edit/$', views.edit_profile_company, name='Profile Edit'),
    url(r'^loginuser/$', views.checkuserlogin, name='login User'),
    url(r'^search/$', views.search_job, name='Search Job'),
    url(r'^logincompany/$', views.checkcompanylogin, name='login company'),
    url(r'^login/user/$', views.login_user, name='user allowed'),
    url(r'^login/company/$', views.login_Company, name='user allowed'),
    url(r'^userprofile/$', views.userprofile, name='profile'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^companyprofile/$', views.companyprofile, name='profile'),

]
