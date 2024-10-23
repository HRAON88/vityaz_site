from rest_framework import serializers
from .models import Group, Schedule

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name', 'trainer', 'kind_of_sport']

class ScheduleSerializer(serializers.ModelSerializer):
    group = GroupSerializer()

    class Meta:
        model = Schedule
        fields = ['group', 'day_of_week', 'start_time', 'end_time']
