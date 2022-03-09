from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from strugglebusapi.models import Rider
from django.core.exceptions import ValidationError
from rest_framework.decorators import action

class RiderView(ViewSet):
    
    def retrieve(self, request, pk):
        
        try:
            rider = Rider.objects.get(pk=pk)
            serializer = RiderSerializer(rider)
            return Response(serializer.data)
        except Rider.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    def list(self, request):
        rider = Rider.objects.all()
        serializer = RiderSerializer(rider, many=True)
        return Response (serializer.data)
    
class RiderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rider
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'email', 'location', 'age', 'bio')