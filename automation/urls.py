from django.conf.urls import url
from .import views

app_name = "articles"

urlpatterns = [

    url(r'^$', views.automation_home, name="automationhome"),


]