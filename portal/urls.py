from django.conf.urls import url
from . import views
app_name = 'portal'

urlpatterns =[
    url(r'^$', views.home.as_view(), name='home'),
    url(r'^login/$', views.LoginUser.as_view(), name='login'),
    url(r'^register/$', views.UserCreationFormView.as_view(), name='register'),

]