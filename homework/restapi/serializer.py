from rest_framework import serializers
from .models import Store


class my_name_Serializer(serializers.Serializer):
    name = serializers.CharField()


class calculatorSerializer(serializers.Serializer):
    action = serializers.ChoiceField(choices=["*", "+", "-", "/"])
    number1 = serializers.IntegerField()
    number2 = serializers.IntegerField()


    def validate(self, data):

        if data['action'] == '/':
            if data['number2'] == 0:
                raise serializers.ValidationError("You can not div to 0")
        return data


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.rate = validated_data.get('rate', instance.rate)
        instance.save()
        return instance

    def create(self, validated_data):
        return Store.objects.create(**validated_data)
