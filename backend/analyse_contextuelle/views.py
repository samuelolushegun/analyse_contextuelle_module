from rest_framework import viewsets
from .models import (
    SWOT, PESTEL,
    StrategicObjective, ProcessMapping,
    RiskOpportunity, ActionPlan
)
from .serializers import (
    SWOTSerializer, PESTELSerializer,
    StrategicObjectiveSerializer, ProcessMappingSerializer,
    RiskOpportunitySerializer, ActionPlanSerializer
)


class SWOTViewSet(viewsets.ModelViewSet):
    queryset = SWOT.objects.all()
    serializer_class = SWOTSerializer

class PESTELViewSet(viewsets.ModelViewSet):
    queryset = PESTEL.objects.all()
    serializer_class = PESTELSerializer


class StrategicObjectiveViewSet(viewsets.ModelViewSet):
    queryset = StrategicObjective.objects.all()
    serializer_class = StrategicObjectiveSerializer

class ProcessMappingViewSet(viewsets.ModelViewSet):
    queryset = ProcessMapping.objects.all()
    serializer_class = ProcessMappingSerializer

class RiskOpportunityViewSet(viewsets.ModelViewSet):
    queryset = RiskOpportunity.objects.all()
    serializer_class = RiskOpportunitySerializer

class ActionPlanViewSet(viewsets.ModelViewSet):
    queryset = ActionPlan.objects.all()
    serializer_class = ActionPlanSerializer

