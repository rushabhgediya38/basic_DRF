from django.urls import path, include
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns
from TestApp1 import views

urlpatterns = [
    path('api/', index, name='index'),
    path('api/<int:pk>/', detailsAll, name='detailsAll'),

    path('api1/', views.CourseListApi.as_view(), name='all_list'),
    path('api1/<int:pk>/', views.CourseInApi.as_view(), name='lists_all'),

    path('api2/', CourseMixinList.as_view(), name='mixinsView'),
    path('api2/<int:pk>/', CourseMixinPkView.as_view(), name='allMixins'),

    path('api3/', SnippetList.as_view(), name='hello'),
    path('api3/<int:pk>/', SnippetDetail.as_view(), name='hello123'),



]

urlpatterns = format_suffix_patterns(urlpatterns)
