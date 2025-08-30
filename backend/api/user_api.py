from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

# If you need user registration, import the relevant serializer
from django.contrib.auth.models import User


class UserLoginAPIView(APIView):
    """
    Handles login by authenticating the user with username/email and password.
    """
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        # Attempt to authenticate the user
        user = authenticate(username=username, password=password)

        if user is not None:
            # If authentication is successful, generate JWT token (if using JWT)
            refresh = RefreshToken.for_user(user)
            return Response({
                'message': 'Login successful',
                'access_token': str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'message': 'Invalid credentials'
            }, status=status.HTTP_400_BAD_REQUEST)


class UserProfileAPIView(APIView):
    """
    Handles fetching and updating the user profile.
    This requires the user to be authenticated.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Access the authenticated user through `request.user`
        user = request.user
        profile_data = {
            'username': user.username,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
        }
        return Response(profile_data, status=status.HTTP_200_OK)

    def put(self, request):
        # Allows the user to update their profile
        user = request.user
        user.first_name = request.data.get('first_name', user.first_name)
        user.last_name = request.data.get('last_name', user.last_name)
        user.email = request.data.get('email', user.email)
        user.save()

        return Response({'message': 'Profile updated successfully'}, status=status.HTTP_200_OK)


class UserRegistrationAPIView(APIView):
    """
    Handles user registration (creating a new user).
    """
    def post(self, request):
        # Extract data from request
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            return Response({"message": "Username already exists."}, status=status.HTTP_400_BAD_REQUEST)

        # Create a new user
        user = User.objects.create_user(username=username, email=email, password=password)

        return Response({
            "message": "User created successfully",
            "username": user.username,
            "email": user.email
        }, status=status.HTTP_201_CREATED)
