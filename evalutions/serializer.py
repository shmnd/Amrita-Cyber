from rest_framework import serializers
from evalutions.models import EvaluationRequest

class EvaluationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = EvaluationRequest
        fields = '__all__'