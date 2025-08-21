from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static

from users.views import RegisterView
from profiles.views import CustomerProfileViewSet, TechnicianProfileViewSet
from workorders.views import WorkOrderViewSet
from ai.views import DiagnosisView
from payments.views import StripePaymentIntentView

schema_view = get_schema_view(
    openapi.Info(
        title="Appliance Repair API",
        default_version="v1",
    ),
    public=True,
)

router = routers.DefaultRouter()
router.register(r"customers", CustomerProfileViewSet)
router.register(r"technicians", TechnicianProfileViewSet)
router.register(r"workorders", WorkOrderViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/diagnosis/', DiagnosisView.as_view(), name='diagnosis'),
    path('api/stripe/intents/', StripePaymentIntentView.as_view(), name='stripe-intent'),
    path('api/', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
