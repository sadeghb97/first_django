from django.contrib.auth.models import User
from rest_framework import serializers


class ProfileUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        # filde username ejbari va 4 taye digar ekhtiarist. username unique khahad bud
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

    def create(self, validated_data):
        obj = super().create(validated_data)
        obj.set_password(validated_data['password'])
        obj.save()
        return obj;
