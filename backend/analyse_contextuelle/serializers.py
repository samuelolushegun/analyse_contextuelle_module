from rest_framework import serializers
from .models import SWOT, PESTEL
from .models import StrategicObjective, ProcessMapping, RiskOpportunity, ActionPlan

class SWOTSerializer(serializers.ModelSerializer):
    class Meta:
        model = SWOT
        fields = '__all__'

class PESTELSerializer(serializers.ModelSerializer):
    class Meta:
        model = PESTEL
        fields = '__all__'

class StrategicObjectiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = StrategicObjective
        fields = '__all__'


class ProcessMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcessMapping
        fields = '__all__'


class RiskOpportunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = RiskOpportunity
        fields = '__all__'


class ActionPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActionPlan
        fields = '__all__'
