from rest_framework import serializers
from dideban.team.models import Team


class TeamSerialize(serializers.ModelSerializer):
    create_date = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Team
        exclude = ["admin"]

    @staticmethod
    def get_create_date(obj):
        return obj.create_date.timestamp() if obj.create_date else None
