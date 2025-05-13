from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class InfoView(APIView):
    @swagger_auto_schema(
        operation_description="Get a greeting message",
        responses={
            200: openapi.Response(
                description="Successful response",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'message': openapi.Schema(type=openapi.TYPE_STRING, description='Greeting message')
                    }
                )
            )
        }
    )
    def get(self, request):
        data = {"message": "Hello its Ashok!"}
        return Response(data=data, status=200)
