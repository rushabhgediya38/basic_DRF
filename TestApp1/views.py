from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.response import Response
from .models import Course
from .serializers import CourseSerializers
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes, authentication_classes, throttle_classes
from rest_framework import status
from rest_framework import permissions

# for class based api
from rest_framework.views import APIView

# for mixins
from rest_framework import mixins
from rest_framework import generics

# for authentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.throttling import UserRateThrottle


class OncePerDayUserThrottle(UserRateThrottle):
    rate = '1/minutes'  # days, Hours


# start function based api
@api_view(['GET', 'POST'])
@throttle_classes([OncePerDayUserThrottle])
# @api_view(http_method_names=['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes((IsAuthenticatedOrReadOnly,))
def index(request):
    if request.method == 'GET':
        course = Course.objects.all()
        serializers = CourseSerializers(course, many=True)
        return Response(serializers.data)

    if request.method == 'POST':
        allData = JSONParser().parse(request)
        serializers = CourseSerializers(data=allData)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticatedOrReadOnly,))
def detailsAll(request, pk):
    try:
        co = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializers = CourseSerializers(co)
        return Response(serializers.data)

    if request.method == 'DELETE':
        co.delete()
        return Response(status=status.HTTP_200_OK)

    if request.method == 'PUT':
        getAllData = JSONParser().parse(request)
        serializer = CourseSerializers(co, data=getAllData)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


# end function based api


# start class based api
class CourseListApi(APIView, LimitOffsetPagination):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        course = Course.objects.all()
        results = self.paginate_queryset(course, request, view=self)
        serializer = CourseSerializers(results, many=True)
        return self.get_paginated_response(serializer.data)
        # return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CourseSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseInApi(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return Course.objects.get(pk=pk)
        except:
            return JsonResponse({'message': 'this id is not available'})

    def get(self, request, pk, format=None):
        course = self.get_object(pk)
        serilaizers = CourseSerializers(course)
        return Response(serilaizers.data)

    def delete(self, request, pk, format=None):
        course = self.get_object(pk)
        course.delete()
        return Response({'message': 'delete'})

    def put(self, request, pk, format=None):
        course = self.get_object(pk)
        course1 = CourseSerializers(course, data=request.data)
        if course1.is_valid():
            course1.save()
            return Response(course1.data)
        else:
            return Response(course1.errors)


# end class based API


# start mixin API
class CourseMixinList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializers
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CourseMixinPkView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                        generics.GenericAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializers

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# end mixin API


class SnippetList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Course.objects.all()
    serializer_class = CourseSerializers
    # permission_classes = [IsAdminUser]
    # authentication_classes = [TokenAuthentication]

    #  override this List method
    def List(self, request):
        queryset = self.get_object()
        serilaizers = CourseSerializers(queryset, many=True)
        return Response(serilaizers.data)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Course.objects.all()
    serializer_class = CourseSerializers

# http POST http://127.0.0.1:8000/api-token-auth/ username='rushabh' password="rushabh"
# http GET http://127.0.0.1:8000/api2/ "Authorization: Token 79eaa107382806937d0ef202566db945327372c8"
# http GET http://127.0.0.1:8000/django-rest-allauth/token/changepassword "Authorization: Token 79eaa107382806937d0ef202566db945327372c8"
