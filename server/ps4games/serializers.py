from rest_framework import serializers
from django.utils import timezone
from ps4games import models


class PS4GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PS4Game
        fields = "__all__"
        read_only_fields = ("created_at", "updated_at")

    def validate_name(self, value):
        if value.isalnum():
            return value
        else:
            raise serializers.ValidationError("Wrong name!")

    def create(self, validated_data):
        print("2: before ser_save")
        obj = super().create(validated_data)
        obj.created_at = timezone.now()
        obj.save()
        print("3: after ser_save")
        return obj

    def update(self, instance, validated_data):
        old_created_at = instance.created_at
        obj = super().update(instance, validated_data)
        obj.created_at = old_created_at
        obj.updated_at = timezone.now()
        obj.save
        return obj
