from rest_framework import serializers
from book_api.models import Book
from django.forms import ValidationError

'''
class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    number_of_pages = serializers.IntegerField(read_only=True)
    publish_date = serializers.DateField(read_only=True)
    quantity = serializers.IntegerField()
'''


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        extra_kwargs = {
            'number_of_pages': {'required': False},
            'publish_date': {'required': False},
        }


def create(self, validated_data):
    return Book.objects.create(**validated_data)


def update(self, instance, validated_data):
    instance.title = validated_data.get('title', instance.title)
    instance.number_of_pages = validated_data.get('number_of_pages', instance.number_of_pages)
    instance.publish_date = validated_data.get('publish_date', instance.publish_date)
    instance.quantity = validated_data.get('quantity', instance.quantity)

    instance.save()
    return instance


def validate(self, validated_data):
    if validated_data['number_of_pages'] > 400 and validated_data['quantity'] > 400:
        raise ValidationError("Too heavy for inventory")
    return validated_data
