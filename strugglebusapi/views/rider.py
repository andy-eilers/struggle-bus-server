from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from strugglebusapi.models import Rider
from django.contrib.auth.models import User
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
        
    def destroy(self, request, pk):
        rider = Rider.objects.get(pk=pk)
        rider.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def update(self, request, pk):
        try:
            rider = Rider.objects.get(pk=pk)
            user = User.objects.get(pk=rider.id)
            user.username = request.data['username']
            user.first_name = request.data['first_name']
            user.last_name = request.data['last_name']
            user.email = request.data['email']
            rider.bio = request.data['bio']
            rider.save()
            user.save()
            """serializer = CreateRiderSerializer(user, request.data['bio'])
            serializer.is_valid(raise_exception=True)
            serializer.save()"""
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except ValidationError as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)  
    
class RiderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rider
        depth = 2
        fields = ('id', 'bio', 'user')
        
class CreateRiderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rider
        fields = ('id', 'bio', 'user')