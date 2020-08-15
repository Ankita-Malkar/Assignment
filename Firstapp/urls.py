from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from Firstapp import views
from django.views.generic import TemplateView


urlpatterns =[url(r'^upload/csv/$', views.upload_csv, name='upload_csv'),
           
    
     url(r'^upload/csv/successful',TemplateView.as_view(
      template_name = 'successful.html')
)
]
   

