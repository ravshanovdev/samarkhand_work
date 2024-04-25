from django.shortcuts import render
from .models import MyResume, Variants, Test
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import MyResumeSerializer, VariantsSerializer, TestSerializer
from rest_framework.generics import ListAPIView
from rest_framework import status
from rest_framework.pagination import PageNumberPagination


class PaginationClass(PageNumberPagination):
    page_size = 2


# views for resume

# add resume

@api_view(["POST"])
def create_resume(request):
    try:
        serializers = MyResumeSerializer(data=request.data)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors)

    except Exception as e:
        return Response([e])


# get all resumes

class ResumeListApiView(ListAPIView):
    pagination_class = PaginationClass
    queryset = MyResume.objects.all()
    serializer_class = MyResumeSerializer


# get your resume

@api_view(["GET"])
def get_my_resume(request):

    if request.user.is_authenticated:
        resume = MyResume.objects.filter(created_by=request.user)

        if resume:
            serializers = MyResumeSerializer(resume)
            return Response(serializers.data)
        else:
            return Response({"message": "Your Resume Not Found.!"}, status=status.HTTP_404_NOT_FOUND)

    else:
        return Response({"error": "You Must Register Our Web Site, After This Try Again.!"}, status=status.HTTP_401_UNAUTHORIZED)


# views for test

@api_view(['POST'])
def create_test(request):
    try:
        serializer = TestSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    except Exception as e:
        return Response([e])


class TestListAPiView(ListAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer


@api_view(['POST'])
def create_variants(request):
    try:
        serializer = VariantsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    except Exception as e:
        return Response([e])






