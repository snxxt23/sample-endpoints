from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny
from .serializer import UserSerializer
from rest_framework.response import Response
from .models import CustomUser
from rest_framework_simplejwt.views import TokenObtainPairView


@api_view(['POST'])
@permission_classes([AllowAny])
def registration_view(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            CustomUser.objects.create_user(
               email = serializer.validated_data['email'],
               first_name = serializer.validated_data['first_name'],
               last_name = serializer.validated_data['last_name'],
               password = serializer.validated_data['password']
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CustomTokenObtainPairView(TokenObtainPairView):
    pass

@api_view(['GET'])
def profile_view(request):
    if request.user.is_authenticated:
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
    return Response(status=status.HTTP_401_UNAUTHORIZED)
