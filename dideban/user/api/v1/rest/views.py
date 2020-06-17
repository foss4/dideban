from django.contrib.auth import authenticate
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet

from utils.common.drf_params import jwt_key

from .serializers import (
    ChangePasswordSerializer, UserProfileSerializer, ResetPasswordSerializer
)
from dideban.user.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class UserProfile(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserProfileSerializer

    @swagger_auto_schema(
        manual_parameters=[jwt_key],
        responses={200: UserProfileSerializer})
    def get(self, request):
        return Response(self.serializer_class(instance=request.user).data)

    @swagger_auto_schema(
        request_body=UserProfileSerializer,
        manual_parameters=[jwt_key],
        responses={status.HTTP_200_OK: UserProfileSerializer}
    )
    def patch(self, request):
        serializer = self.serializer_class(
            request.user,
            data=request.data,
            partial=True,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class UserChangePassword(APIView):

    permission_classes = [IsAuthenticated]
    serializer_class = ChangePasswordSerializer

    @swagger_auto_schema(
        manual_parameters=[jwt_key],
        request_body=ChangePasswordSerializer,
        responses={205: None}
    )
    def put(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        if user := authenticate(
            request,
            username=request.user.username,
            password=data["old_password"],
        ):
            user.set_password(data["new_password"])
            user.save()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)


class UserResetPassword(APIView):
    serializer_class = ResetPasswordSerializer
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        request_body=ResetPasswordSerializer,
        responses={205: None}
    )
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        if user := User.objects.filter(username=data["email"]):
            user = user.first()
            rand_password = User.objects.make_random_password()
            send_mail(
                subject=_("Reset Password"),
                message=_("Your New Password Is = ") + rand_password,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[data["email"]],
            )
            user.set_password(rand_password)
        raise NotFound()
