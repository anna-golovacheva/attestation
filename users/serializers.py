from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from users.models import User
from users.services import num_in_password
from users.validators import CheckEmailDomainValidator


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'username', 'email', 'password', 'date_of_birth')
        extra_kwargs = {
            'password': {'write_only': True},
        }

        validators = [CheckEmailDomainValidator(field='email')]

    def validate_password(self, value):
        if len(value) >= 8 and num_in_password(value):
            return make_password(value)
        raise serializers.ValidationError('Пароль должен состоять из 8 и более символов и включать цифры')

    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'], email=validated_data['email'], password=validated_data['password'], date_of_birth=validated_data['date_of_birth'])
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'date_of_birth'
        )
