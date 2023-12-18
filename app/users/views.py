from rest_framework.response import Response
from rest_framework import status, serializers
from rest_framework.views import APIView
from rest_framework import generics
import django_filters.rest_framework
from .serializers import UserSerializer, HomeSerializer, RoleSerializer
from django.contrib.auth import authenticate
from .models import CustomUser, Home, Role
from .filters import UserFilter
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import UserDetailPermission, IsAdminOrSuperUser


# Create your views here.

# LOGIN / REGISTER Views


class LoginView(APIView):
    """Retrieves a token for a user with the given credentials"""

    permission_classes = ()

    class InputSerializer(serializers.Serializer):
        email = serializers.EmailField()
        password = serializers.CharField()

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data["email"]
            password = serializer.validated_data["password"]
            user = authenticate(email=email, password=password)
            if user:
                return Response(
                    {"token": user.auth_token.key}, status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserCreate(generics.CreateAPIView):
    """Creates a new user"""

    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer


# Lists
class HomeListView(generics.ListAPIView):
    """Lists all homes"""

    permission_classes = ()
    authentication_classes = ()
    queryset = Home.objects.all()
    serializer_class = HomeSerializer


class RoleListView(generics.ListAPIView):
    """Lists all roles"""

    permission_classes = ()
    authentication_classes = ()
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


# Users data


class CurrentUserView(APIView):
    """Retrieves the data of the current user"""

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class UserListView(generics.ListAPIView):
    """Lists all users"""

    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = UserFilter
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Retrieves, updates or deletes a user"""

    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    lookup_field = "id"
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, UserDetailPermission]


class UserChangeStatusView(APIView):
    """Changes the status of a user"""

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrSuperUser]

    def post(self, request, id):
        user = CustomUser.objects.get(id=id)
        if not 'status' in request.data:
            return Response(
                {"error": "Status field is required"}, status=status.HTTP_400_BAD_REQUEST
            )
        new_status = request.data["status"]
        if new_status not in ["Active", "Pending", "Frozen"]:
            return Response(
                {"error": "Status must be Active, Pending or Frozen"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        user.status = new_status
        user.save()
        return Response({'status': new_status},status=status.HTTP_200_OK)


# Home data and role data


class HomeView(generics.RetrieveAPIView):
    """Retrieves, updates or deletes a home"""

    permission_classes = ()
    authentication_classes = ()
    queryset = Home.objects.all()
    serializer_class = HomeSerializer
    lookup_field = "id"


class RoleView(generics.RetrieveAPIView):
    """Retrieves, updates or deletes a role"""

    permission_classes = ()
    authentication_classes = ()
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    lookup_field = "id"
