import openai
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import DiagnosisRequestSerializer

class DiagnosisView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = DiagnosisRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        prompt = f"Appliance type: {data['appliance_type']}\nModel: {data.get('model_number','')}\nIssue: {data['issue_description']}\nProvide a possible diagnosis."
        try:
            resp = openai.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role":"user","content":prompt}])
            suggestion = resp.choices[0].message.content
        except Exception as e:
            suggestion = str(e)
        return Response({"suggestion": suggestion})
