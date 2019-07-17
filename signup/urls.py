from django.urls import path

from . import views

app_name = 'signup'
urlpatterns = [
    path('', views.Base.as_view(), name='signup'),
    path('signup', views.SignUp.as_view(), name='signup'),
    path('signin', views.SignIn.as_view(), name='signin'),
    path('savedata', views.savedata, name='savedata'),
    path('datacheck',views.check_data , name='check_data')
]
