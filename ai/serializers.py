from rest_framework import serializers

class DiagnosisRequestSerializer(serializers.Serializer):
    appliance_type = serializers.CharField()
    model_number = serializers.CharField(required=False, allow_blank=True)
    issue_description = serializers.CharField()
    files = serializers.ListField(
        child=serializers.FileField(), required=False
    )
