from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from strugglebusapi.models import Post, Bus, Rider, Struggle
from django.core.exceptions import ValidationError

class PostView(ViewSet):
    
    def retrieve(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
            serializer = PostSerializer(post)
            return Response(serializer.data)
        except Post.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    def list(self, request):
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        data = request.data
        rider = Rider.objects.get(user=request.auth.user)
        data['rider'] = rider.id
        try:
            serializer = CreatePostSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def update(self, request, pk):
        try:
            post = Post.objects.get(pk=pk)
            serializer = CreatePostSerializer(post, data=request.data)
            serializer.is_valid(raise_exception=True)
            post = serializer.save()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except ValidationError as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)    
    
    
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        depth = 2
        fields = ('id', 'rider', 'title', 'bus', 'struggle', 'description', 'date', 'comment_set')
        
class CreatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'rider', 'title', 'bus', 'struggle', 'description', 'date')