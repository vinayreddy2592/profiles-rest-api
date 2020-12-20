from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, put, patch, delete)',
            'Is similat to a traditional Django view',
            'Gives you most control of your application logic',
            'Is mappped manullay to URLs',
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})
