from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from strugglebusapi.models import Comment, Rider
from django.core.exceptions import ValidationError

class CommentView(ViewSet):
    
    def retrieve(self, request, pk):
        try:
            comment = Comment.objects.get(pk=pk)
            serializer = CommentSerializer(comment)
            return Response(serializer.data)
        except Comment.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
    def list(self, request):
            comment = Comment.objects.all()
            serializer = CommentSerializer(comment, many=True)
            return Response(serializer.data)
    
    def create(self, request):
        data = request.data
        rider = Rider.objects.get(user=request.auth.user)
        data['rider'] = rider.id
        try:
            serializer = CreateCommentSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)
        
    def destroy(self, request, pk):
        comment = Comment.objects.get(pk=pk)
        comment.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def update(self, request, pk):
        try:
            comment = Comment.objects.get(pk=pk)
            serializer = CreateCommentSerializer(comment, data=request.data)
            serializer.is_valid(raise_exception=True)
            comment = serializer.save()
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except ValidationError as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)    
    
    
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        depth = 1
        fields = ('id', 'rider', 'post', 'body', 'date')
        
class CreateCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'rider', 'post', 'body', 'date')