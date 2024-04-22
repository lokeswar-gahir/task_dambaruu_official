from django.urls import path, include
from .views import *


urlpatterns = [
    path('sign-up/', Default_User_Registeration_View.as_view(), name='sign-up'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    # path('', include('django.contrib.auth.urls')),

]
