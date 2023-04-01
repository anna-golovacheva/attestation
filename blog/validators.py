from rest_framework import serializers


class ForbiddenWordsValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        header = value.get('header')
        if header:
            for word in ['ерунда', 'глупость', 'чепуха']:
                if word in header:
                    raise serializers.ValidationError('Запрещенное слово в заголовке')
