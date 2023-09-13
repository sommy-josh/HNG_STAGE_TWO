from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

    def validate_name(self, value):
        # Add your custom validation logic here
        if not value.isalpha():
            raise serializers.ValidationError("Name should only contain alphabetic characters.")
        return value
