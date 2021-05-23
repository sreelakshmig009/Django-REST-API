from rest_framework import serializers

from .models import Advisor

class AdvisorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Advisor
        fields = ('name', 'url')
