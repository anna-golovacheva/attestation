from rest_framework import serializers

from users.services import email_domain


class CheckEmailDomainValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        email = value.get('email')
        if email_domain(email) is None:
            raise serializers.ValidationError('Разрешены домены mail.ru или yandex.ru')
