from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^jobseeker/$', views.get_name, name='register'),
	url(r'^jobseeker/thanks/$',views.thanks,name="thanx"),
]
