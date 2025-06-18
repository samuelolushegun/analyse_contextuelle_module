from rest_framework.routers import DefaultRouter
from .views import (
    SWOTViewSet, PESTELViewSet,
    StrategicObjectiveViewSet, ProcessMappingViewSet,
    RiskOpportunityViewSet, ActionPlanViewSet
)

router = DefaultRouter()
router.register(r'swot', SWOTViewSet)
router.register(r'pestel', PESTELViewSet)
router.register(r'objectives', StrategicObjectiveViewSet, basename='objective')
router.register(r'process-mappings', ProcessMappingViewSet, basename='process-mapping')
router.register(r'risk-opportunities', RiskOpportunityViewSet, basename='risk-opportunity')
router.register(r'action-plans', ActionPlanViewSet, basename='action-plan')

urlpatterns = router.urls
