"""View module for handling requests about bus types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from strugglebusapi.models import Bus

class BusView(ViewSet):
    
    def retrieve(self, request, pk):
        try:
            bus = Bus.objects.get(pk=pk)
            serializer = BusSerializer(bus)
            return Response(serializer.data)
        except Bus.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_Not_Found)
        
    def list(self, request):
        bus = Bus.objects.all()
        serializer = BusSerializer(bus, many=True)
        return Response(serializer.data)
    
class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = ('id', 'label')