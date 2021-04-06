from django.urls import path, include
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns
from TestApp1 import views
from .models import Course
from .serializers import CourseSerializers

from rest_framework.authtoken import views as authviews
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('api/', index, name='index'),
    path('api/<int:pk>/', detailsAll, name='detailsAll'),

    path('api1/', views.CourseListApi.as_view(), name='all_list'),
    path('api1/<int:pk>/', views.CourseInApi.as_view(), name='lists_all'),

    path('api2/', CourseMixinList.as_view(), name='mixinsView'),
    path('api2/<int:pk>/', CourseMixinPkView.as_view(), name='allMixins'),

    path('api3/', SnippetList.as_view(), name='hello'),
    # path('api3/', SnippetList.as_view(queryset=Course.objects.all(), serializer_class=CourseSerializers),
    #      name='hello'),
    path('api3/<int:pk>/', SnippetDetail.as_view(), name='hello123'),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', authviews.obtain_auth_token, name='api-tokn-auth'),
    path('django-rest-allauth/', include('django_rest_allauth.api.urls')),

    # JWT TOKEN
    path('api/token/all/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/all/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
