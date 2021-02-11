from rest_framework import serializers

from Data import models


class FooSerializer(serializers.ModelSerializer):
    """Serializes Foo items"""

    class Meta:
        model = models.Foo
        fields = '__all__'

class FooBarSerializer(serializers.ModelSerializer):
    """Serializes FooBar items"""

    class Meta:
        model = models.FooBar
        fields = '__all__'

