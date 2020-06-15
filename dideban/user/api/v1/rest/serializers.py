from rest_framework import serializers

from dideban.user.models import User


class UserProfileSerializer(serializers.ModelSerializer):
    email = serializers.ReadOnlyField()
    date_joined = serializers.SerializerMethodField(read_only=True)
    last_login = serializers.SerializerMethodField(read_only=True)
    is_staff = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = [
            "email", "is_staff", "date_joined",
            "first_name", "last_name", "last_login",
        ]

    @staticmethod
    def get_last_login(obj):
        return obj.last_login.timestamp() if obj.last_login else None

    @staticmethod
    def get_date_joined(obj):
        return obj.date_joined.timestamp() if obj.date_joined else None


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True, max_length=50)
    new_password = serializers.CharField(required=True, max_length=50)


class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()