from django.shortcuts import render
from .models import MyProfil
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProfileSerializer
from rest_framework.generics import ListAPIView
from rest_framework import status


@api_view(["POST"])
def create_profile(request):
    serializers = ProfileSerializer(data=request.data)

    if serializers.is_valid():
        serializers.save(created_by=request.user)
        return Response(serializers.data)
    return Response(serializers.errors)


class ProfileListApiView(ListAPIView):
    queryset = MyProfil.objects.all()
    serializer_class = ProfileSerializer


class GetMyProfileView(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            profiles = MyProfil.objects.filter(created_by=request.user)  # Assuming UserProfile model

            if profiles:
                if len(profiles) == 1:
                    # Single profile: use single object serialization
                    serializer = ProfileSerializer(profiles.first())
                else:
                    # Multiple profiles: use many=True
                    serializer = ProfileSerializer(profiles, many=True)
                return Response(serializer.data)
            else:
                return Response({"message": "Your profile was not found."}, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response({"error": "You must be logged in to access your profile."}, status=status.HTTP_401_UNAUTHORIZED)

