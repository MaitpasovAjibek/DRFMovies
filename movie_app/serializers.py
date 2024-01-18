from rest_framework import serializers
from .models import Movie,Director,Rewiew

class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'id title description duration duration director'.split()


class DirectorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'id name'.split()


class RewiewSerilizers(serializers.ModelSerializer):
    class Meta:
        model = Rewiew
        fields = 'id text'.split()