from rest_framework import serializers
from .models import Cloth, Category


# class ClothSerializer(serializers.ModelSerializer):
#
#     def create(self, validated_data):
#         return Cloth.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.brand = validated_data.get('brand', instance.brand)
#         instance.price = validated_data.get('price', instance.price)
#         instance.category_id = validated_data.get('category_id', instance.category_id)
#         instance.save()
#         return instance
#
#     def delete(self, pk):
#         instance = Cloth.objects.get(pk=pk)
#         instance.delete()
#
#     class Meta:
#         model = Cloth
#         fields = ('id', 'name', 'brand', 'price', 'category_id')

class ClothSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Cloth
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')
