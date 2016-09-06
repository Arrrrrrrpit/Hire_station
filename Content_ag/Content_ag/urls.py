from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
	url(r'^Scriber/', include('Content_Scriber.urls')),
	url(r'^admin/', admin.site.urls),
]
