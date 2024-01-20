from rest_framework.serializers import ModelSerializer

from .models import Post, CustomUser

class AuthorSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username',)


class PostSerializer(ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Post
        fields = "__all__"
    
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['likes'] = [user.username for user in self.instance.likes.all()]
        return ret