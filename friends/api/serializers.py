from rest_framework import serializers
from friends.models import Friend


class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = ['id', 'first_name', 'last_name', 'phone_number', 'city', 'birthday_date']
        read_only_fields = ['id']
        extra_kwargs = {
            'first_name': {'required': False},
            'last_name': {'required': False},
            'phone_number': {'required': False},
            'city': {'required': False},
            'birthday_date': {'required': False},
        }

    def to_internal_value(self, data):
        allowed_fields = set(self.Meta.fields) - set(self.Meta.read_only_fields)
        extra_fields = set(data.keys()) - allowed_fields

        if extra_fields:
            raise serializers.ValidationError(
                {field: "This field is not allowed." for field in extra_fields}
            )

        return super().to_internal_value(data)
