"""View module for handling requests about bus types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from strugglebusapi.models import Struggle

class StruggleView(ViewSet):
    
    def retrieve(self, request, pk):
        try:
            struggle = Struggle.objects.get(pk=pk)
            serializer = StruggleSerializer(struggle)
            return Response(serializer.data)
        except Struggle.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_Not_Found)
        
    def list(self, request):
        struggle = Struggle.objects.all()
        serializer = StruggleSerializer(struggle, many=True)
        return Response(serializer.data)
    
class StruggleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Struggle
        fields = ('id', 'label')