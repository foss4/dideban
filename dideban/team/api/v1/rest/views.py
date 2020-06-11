from django.db.models.query import QuerySet
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from dideban.team.models import Team
from utils.common.drf_params import jwt_key

from .serializers import TeamSerialize


@method_decorator(name='retrieve', decorator=swagger_auto_schema(
    manual_parameters=[jwt_key],
))
@method_decorator(name='create', decorator=swagger_auto_schema(
    manual_parameters=[jwt_key],
))
@method_decorator(name='partial_update', decorator=swagger_auto_schema(
    manual_parameters=[jwt_key],
))
@method_decorator(name='update', decorator=swagger_auto_schema(
    manual_parameters=[jwt_key],
))
@method_decorator(name='list', decorator=swagger_auto_schema(
    manual_parameters=[jwt_key],
))
@method_decorator(name='destroy', decorator=swagger_auto_schema(
    manual_parameters=[jwt_key],
))
class TeamViewSet(ModelViewSet):
    serializer_class = TeamSerialize
    permission_classes = [IsAdminUser]
    queryset = Team.objects.all()

    def perform_create(self, serializer):
        serializer.save(admin=self.request.user)

    def get_queryset(self):
        assert self.queryset is not None, (
            "'%s' should either include a `queryset` attribute, "
            "or override the `get_queryset()` method."
            % self.__class__.__name__
        )

        queryset = self.queryset
        if isinstance(queryset, QuerySet):
            queryset = queryset.filter(admin=self.request.user)
        return queryset
