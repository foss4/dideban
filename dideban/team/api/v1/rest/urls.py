from django.urls import path
from .views import TeamViewSet


urlpatterns = [
    path('', TeamViewSet.as_view(
        {'get': 'list', "post": "create"}
    ), name='team_list_create'),
    path('<int:pk>/', TeamViewSet.as_view(
        {'get': 'retrieve', "put": "update", "delete": "destroy"}
    ), name='team_get_update'),
]
