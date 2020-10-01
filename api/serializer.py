from .models import Posts
from rest_framework import serializers


class PostsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Posts
        fields = ['boast', 'text', 'upvote', 'downvote', 'postdate', 'score']



        