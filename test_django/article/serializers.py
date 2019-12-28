from rest_framework import serializers

from .models import Article


"""
class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)
    description = serializers.CharField()
    body = serializers.CharField()
    author_id = serializers.IntegerField()

    def create(self, validated_data):
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description',
                                                  instance.description)
        instance.body = validated_data.get('body', instance.body)
        instance.author_id = validated_data.get('author_id',
                                                instance.author_id)

        instance.save()
        return instance
"""


# When we use ModelSerializer we get methods 'create' and 'update'
# and the same set of validators by default
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'body', 'description', 'author_id')
