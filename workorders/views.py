from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.permissions import IsAuthenticated
from .models import WorkOrder, WorkOrderMedia
from .serializers import WorkOrderSerializer, WorkOrderMediaSerializer

class WorkOrderViewSet(viewsets.ModelViewSet):
    queryset = WorkOrder.objects.all()
    serializer_class = WorkOrderSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def perform_create(self, serializer):
        workorder = serializer.save()
        files = self.request.FILES.getlist('files')
        for f in files:
            WorkOrderMedia.objects.create(workorder=workorder, file=f)
