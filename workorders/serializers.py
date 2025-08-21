from rest_framework import serializers
from .models import WorkOrder, WorkOrderMedia

class WorkOrderMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkOrderMedia
        fields = ("id", "file")

class WorkOrderSerializer(serializers.ModelSerializer):
    media = WorkOrderMediaSerializer(many=True, read_only=True)

    class Meta:
        model = WorkOrder
        fields = (
            "id",
            "customer",
            "technician",
            "appliance_type",
            "model_number",
            "issue_description",
            "status",
            "created_at",
            "updated_at",
            "media",
        )
