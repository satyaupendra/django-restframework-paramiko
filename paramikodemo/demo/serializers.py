from rest_framework import serializers
from .models import ParamikoModel
class ParamikoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=ParamikoModel
        fields=["user_name","password","ip","pathToFile"]