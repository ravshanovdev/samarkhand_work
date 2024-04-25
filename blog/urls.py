from django.urls import path
from .views import create_test, TestListAPiView, create_variants, create_resume, get_my_resume

urlpatterns = [
    path('create_test/', create_test, ),
    path('test_list/', TestListAPiView.as_view(), ),
    path('create_variants/', create_variants, ),
    path('create_resume/', create_resume, ),
    path('get_my_resume/', get_my_resume, ),

]
