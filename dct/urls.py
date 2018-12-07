from django.conf.urls import url,include
from .views import HomePage

urlpatterns = [
   url('',HomePage.as_view(), name = 'home')
]