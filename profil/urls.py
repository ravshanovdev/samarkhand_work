from django.urls import path
from .views import create_profile, ProfileListApiView, GetMyProfileView

urlpatterns = [
    path('create_profile/', create_profile, ),
    path('get_my_profile/', GetMyProfileView.as_view(), ),
    path('profile_list/', ProfileListApiView.as_view(), ),

]

