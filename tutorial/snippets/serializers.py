from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User


class SnippetSerializer(serializers.ModelSerializer):
    # The untyped ReadOnlyField is always read-only, and will be used for serialized representations, but will not be used for updating model instances when they are deserialized.
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Snippet
        # required data input fields when deserializing (when calling serializer.save())
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style', 'owner')


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        # 'snippets' is a reverse relationship on the User model
        fields = ('id', 'username', 'snippets') # snippets refers to related_name
