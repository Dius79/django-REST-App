import stripe
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.conf import settings
from .serializers import PaymentIntentSerializer

stripe.api_key = 'sk_test_12345'  # placeholder

class StripePaymentIntentView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = PaymentIntentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        # In this demo environment we return a mocked client secret instead of
        # performing a live Stripe API call.
        client_secret = "pi_test_secret"
        return Response({"client_secret": client_secret})
