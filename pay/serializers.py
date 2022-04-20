from rest_framework import serializers
from .models import payment
class PaySerializer(serializers.ModelSerializer):
    class Meta:
        model = payment
        fields = ['userid', 'fullName', 'phone', 'email', 'sum', 'pageCode','processId','processToken']


class thankSerializer(serializers.ModelSerializer):
    # thanks = PaySerializer(many=True,read_only=True)
    class Meta:
        model = payment
        fields = ['userid','pageCode','processId','processToken']