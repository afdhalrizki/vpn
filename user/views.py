from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import OwnerSerializer, CompanySerializer, EmployeeSerializer
from .models import User
from .permissions import IsOwnerOrReadOnly

class OwnerCreateView(APIView):
    """Handles sign-up Owners."""
    authentication_classes = ()

    def post(self, request):
        serializer = OwnerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class UserListView(generics.ListAPIView):
    """Handles listing Users."""
    authentication_classes = ()
    queryset = User.objects.all()
    
    def get_serializer_class(self):
        return OwnerSerializer

class CreateCompanyView(generics.CreateAPIView):
     """Handles creating Company."""
     permission_classes = (IsOwnerOrReadOnly,)
     
     def post(self, request, *args, **kwargs):
            serializer = CompanySerializer(data=request.data)
            if serializer.is_valid():
                self.perform_create(serializer)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     
class EmployeeCreateView(generics.CreateAPIView):
    """Handles creating Employees."""
    permission_classes = (IsOwnerOrReadOnly,)
    serializer_class = EmployeeSerializer

    def post(self, request, *args, **kwargs):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)