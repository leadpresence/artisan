from django.urls import path
from artisanstuple import views



urlpatterns=[
   # path("toolbox2/",artisanstuple/img/toolbox2.png,name="toolbox2"),
    path("",views.home, name="home"),
    
]
