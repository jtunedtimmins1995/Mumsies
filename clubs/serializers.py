from clubs.models import Club, Deals
from rest_framework import serializers



class ClubSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Club
        fields = ['id', 'name', 'city', 'website']
        


class DealSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Deals
        fields = ['id', 'club', 'description', 'code', 'startTime', 'endTime']