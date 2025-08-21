from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import CustomerProfile, TechnicianProfile
from .serializers import CustomerProfileSerializer, TechnicianProfileSerializer

class CustomerProfileViewSet(viewsets.ModelViewSet):
    queryset = CustomerProfile.objects.all()
    serializer_class = CustomerProfileSerializer
    permission_classes = [IsAuthenticated]

class TechnicianProfileViewSet(viewsets.ModelViewSet):
    queryset = TechnicianProfile.objects.all()
    serializer_class = TechnicianProfileSerializer
    permission_classes = [IsAuthenticated]
