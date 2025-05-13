from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class SecondAPIView(APIView):
    @swagger_auto_schema(
        operation_description="Add two integers and return their sum",
        manual_parameters=[
            openapi.Parameter(
                'a',
                openapi.IN_QUERY,
                description="First integer",
                type=openapi.TYPE_INTEGER,
                required=True
            ),
            openapi.Parameter(
                'b',
                openapi.IN_QUERY,
                description="Second integer",
                type=openapi.TYPE_INTEGER,
                required=True
            )
        ],
        responses={
            200: openapi.Response(
                description="Successful response",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'message': openapi.Schema(type=openapi.TYPE_STRING, description='API message'),
                        'parameters': openapi.Schema(
                            type=openapi.TYPE_OBJECT,
                            properties={
                                'a': openapi.Schema(type=openapi.TYPE_INTEGER),
                                'b': openapi.Schema(type=openapi.TYPE_INTEGER)
                            }
                        ),
                        'sum': openapi.Schema(type=openapi.TYPE_INTEGER, description='Sum of a and b')
                    }
                )
            ),
            400: openapi.Response(
                description="Bad request",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'error': openapi.Schema(type=openapi.TYPE_STRING)
                    }
                )
            )
        }
    )
    def get(self, request):
        # Get parameters from query string
        a = request.query_params.get('a')
        b = request.query_params.get('b')
        
        # Check if both parameters are provided
        if a is None or b is None:
            return Response(
                {"error": "Both parameters 'a' and 'b' are required"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            # Convert parameters to integers
            a = int(a)
            b = int(b)
            
            # Calculate sum
            result = a + b
            
            return Response({
                "message": "I am the second API",
                "parameters": {
                    "a": a,
                    "b": b
                },
                "sum": result
            }, status=status.HTTP_200_OK)
            
        except ValueError:
            return Response(
                {"error": "Parameters 'a' and 'b' must be integers"},
                status=status.HTTP_400_BAD_REQUEST
            ) 