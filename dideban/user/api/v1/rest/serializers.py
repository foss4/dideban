from rest_framework import serializers
from dideban.user.models import User


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["email", "is_staff", "date_joined"]
