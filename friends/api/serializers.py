from rest_framework import serializers
from friends.models import Friend


class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = ['id', 'first_name', 'last_name', 'phone_number', 'city', 'birthday_date']
        read_only_fields = ['id']

    def get_fields(self):
        fields = super().get_fields()
        if self.context['request'].method == 'PUT':
            for field_name, field in fields.items():
                field.required = False
        return fields

    def to_internal_value(self, data):
        allowed_fields = set(self.Meta.fields) - set(self.Meta.read_only_fields)
        extra_fields = set(data.keys()) - allowed_fields

        if extra_fields:
            raise serializers.ValidationError(
                {field: "This field is not allowed." for field in extra_fields}
            )

        return super().to_internal_value(data)
