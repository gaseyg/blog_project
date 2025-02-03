from rest_framework import serializers
from blog.models import User, Post


# сериалайзер регистрации пользователя
class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'email',
            'first_name',
            'last_name',
        )


def create(self, validated_data):
    user = User.objects.create(
        username=validated_data['username'],
        email=validated_data['email'],
        first_name=validated_data['first_name'],
        last_name=validated_data['last_name'],
    )
    user.set_password(validated_data['password'])
    user.save()

    return user


# сериалайзер для вывода списка юзер
class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
        )


# сериалайзер для вывода списка постов конкретного пользователя
class UserPostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "body",
            "created_at",
        )


# сер-ер для получения инфы о конкретном юзере
class UserInfoSerializer(serializers.ModelSerializer):
    posts = UserPostListSerializer(many=True)

    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'posts'
        )


# сериалайзер для сокращенной инфы об авторе
class UserShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
             "id",
             "first_name",
             "last_name",
        )


# сериализатор для вывода всех постов
class PostListSerializer(serializers.ModelSerializer):
    author = UserShortSerializer()
    body = serializers.SerializerMethodField()

    class Meta:
        model = Post

        fields = (
            'id',
            'author',
            'title',
            'body',
            'created_at',
        )

    def get_body(self, obj) -> str:
        if len(obj.body) > 120:
            return obj.body[:120] + "..."
        return obj.body


# сериализатор для вывод информации о конкретном посте
class PostInfoSerializer(serializers.ModelSerializer):
    author = UserShortSerializer()
    my_reaction = serializers.SerializerMethodField()

    class Meta:
        model = Post

        fields = (
            'id',
            'author',
            'title',
            'body',
            'my_reaction',
            'created_at',
        )

        def get_my_reaction(self, obj) -> str:
            reaction = self.context['request'].user.reactions.filter(post=obj).last()
            return reaction.value if reaction else ''


class PostCreateUpdateSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )

    class Meta:
        model = Post
        fields = (
            'id',
            'author',
            'title',
            'body',
        )