from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include("dideban.user.api.v1.rest.urls"), name="user"),
    path('team/', include("dideban.team.api.v1.rest.urls"), name="team"),
]

if settings.DEBUG:
    schema_view = get_schema_view(
        openapi.Info(
            title="Dideban API",
            default_version='v1',
            contact=openapi.Contact(email="abtin@riseup.net"),
            license=openapi.License(
                name="AFFERO GENERAL PUBLIC LICENSE Version 3"
            ),
        ),
        public=True,
        permission_classes=(permissions.AllowAny,),
    )
    urlpatterns += [
        url(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
        url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0),
            name='schema-swagger-ui'),
        url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0),
            name='schema-redoc'),
    ]
