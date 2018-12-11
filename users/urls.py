from django.urls import path
from users import views

'''
    Add links to user dashborad here do not add additional home
    url as that will redirect to the users/views/home.html
    '''
urlpatterns=[
    
    path("artisan/",views.artisan,name="artisan")

]