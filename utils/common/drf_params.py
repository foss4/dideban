from drf_yasg import openapi

jwt_key = openapi.Parameter(
    'Authorization',
    openapi.IN_HEADER,
    description='jwt token',
    type=openapi.TYPE_STRING,
    required=True,
    default="Bearer access_token"
)
