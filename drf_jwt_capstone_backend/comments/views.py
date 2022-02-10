 #! Comment Views
 #TODO for production change authetications back.
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Comment
from .models import Reply
from .serializers import CommentSerializer
from .serializers import ReplySerializer
from django.contrib.auth.models import User
from .serializers import UserSerializer

# Create your views here.

@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_comments(request, video_id):
    comments = Comment.objects.filter(video_id=video_id)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny]) #!IsAuthenticated
def get_user(request, user_id):
    user = User.objects.get(id=user_id)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([AllowAny]) #!IsAuthenticated
def user_comments(request):
    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([AllowAny]) #!IsAuthenticated
def update_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    serializer = CommentSerializer(comment, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([AllowAny]) #!IsAuthenticated
def delete_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    if request.user.id == comment.user.id:
        serializer = CommentSerializer(comment, many=False)
        comment.delete()
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
@permission_classes([AllowAny]) #!IsAuthenticated
def post_reply(request, comment_id):
    serializer = ReplySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([AllowAny]) #!IsAuthenticated
def user_replies(request, comment_id):
    replies = Reply.objects.filter(comment_id=comment_id)
    serializer = ReplySerializer(replies, many=True)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([AllowAny]) #!IsAuthenticated
def update_reply(request, reply_id):

    reply = Reply.objects.get(id=reply_id)
    if request.user.id == reply.user.id:
        serializer = ReplySerializer(reply, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(['DELETE'])
@permission_classes([AllowAny]) #!IsAuthenticated
def delete_reply(request, reply_id):
    reply = Reply.objects.get(id=reply_id)
    if request.user.id == reply.user.id:
        serializer = ReplySerializer(reply, many=False)
        reply.delete()
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
