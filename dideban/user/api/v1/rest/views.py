from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from utils.common.drf_params import jwt_key

from .serializers import UserProfileSerializer


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
