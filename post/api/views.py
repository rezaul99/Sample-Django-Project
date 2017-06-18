from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import BlogPostSerializer
from post.models import *


class BlogPostAPIView(APIView):

    def get(self, request, format=None):
        qs = BlogPost.objects.all().order_by('-title')
        serializer = BlogPostSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BlogPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)