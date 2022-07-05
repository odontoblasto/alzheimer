from django.urls import path,include
from .views import UserRegisterView,CreateProfilePageView




app_name = 'members'
urlpatterns=[

    path('',include('main.urls')),
    path("register/", UserRegisterView.as_view(),name="register"),
    path('create_profile_page/',CreateProfilePageView.as_view(),name='create_profile_page'),
    #path('<int:pk>/edit_profile_page/',EditProfilePageView.as_view(),name='edit_profile-page'),
 
    ]