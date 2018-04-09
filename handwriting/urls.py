from django.conf.urls import url
from . import views

app_name='handwriting'

urlpatterns=[
  url(r'^hand/$',views.text)
]
