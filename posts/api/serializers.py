from rest_framework import serializers
from posts.models import Post
from users.api.serializers import UserSerializer
from categories.api.serializers import CategorySerializer


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    category = CategorySerializer()

    class Meta:
        model = Post
        fields = ['title', 'content', 'slug', 'miniature', 'created_at', 'published', 'user', 'category']
