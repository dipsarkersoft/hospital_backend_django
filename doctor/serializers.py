from rest_framework import serializers

from .models import Doctor,Speacialization,Desigation,AvailableTime,Review



        
class SpeacializationSer(serializers.ModelSerializer):
    class Meta:
        model=Speacialization
        fields='__all__'


class DesigationSer(serializers.ModelSerializer):
    class Meta:
        model=Desigation
        fields='__all__'

class AvailableTimeSer(serializers.ModelSerializer):
    class Meta:
        model=AvailableTime
        fields='__all__'

class ReviewSer(serializers.ModelSerializer):
    class Meta:
        model=Review
        fields='__all__'




class DoctorSer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    designation = serializers.StringRelatedField(many=True,read_only=True)
    specialization = serializers.StringRelatedField(many=True,read_only=True)
    available_time = serializers.StringRelatedField(many=True,read_only=True)

    class Meta:
        model = Doctor
        fields = '__all__'