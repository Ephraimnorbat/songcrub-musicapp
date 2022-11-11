from .models import artiste
#from rest_framework import artiste
from rest_framework import serializers


class artisteSerializers(serializers.ModelSerializer):

    class Meta:
        model = artiste
        fields = ['artist','song','artiste_id']
    #fields = '__all__'
