from rest_framework import serializers
from .models import UserSubmission

class UserSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSubmission
        fields = ['name', 'email']  # These fields should match the React form fields
