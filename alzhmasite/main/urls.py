from django.urls import path

from .forms import EditProfileForm
from .views import HomeView,IndexView,ProjetoAlzhmaView,InfoSiteView
from .import views
from django.contrib.auth import views as auth_views


app_name = 'main'
urlpatterns=[
    path("",HomeView.as_view(),name='home'),
    path("index/",IndexView.as_view(),name='index'),
    path("projeto/",ProjetoAlzhmaView.as_view(),name='projeto'),
    path("info_site/",InfoSiteView.as_view(),name='info_site'),
 
    #path("register/", UserRegisterView.as_view(),name="register"),
    #path('main/create_profile_page/',CreateProfilePageView.as_view(),name='create_profile_page'),
    #path('<int:pk>/edit_profile_page/',EditProfilePageView.as_view(),name='edit_profile-page'),
 
    ]