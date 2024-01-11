from rest_framework import serializers
from user.models import User, Company
from six import text_type

from rest_framework_simplejwt.tokens import RefreshToken

class OwnerSerializer(serializers.ModelSerializer):
    """Serializer for owner objects."""
    class Meta:
        model = User
        fields = ["id", "email", "username", "user_type"]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create(email=validated_data['email'],
                                       username=validated_data['email'],
                                       user_type='OWNER',
                                         )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class CompanySerializer(serializers.ModelSerializer):
    tokens = serializers.SerializerMethodField()

    class Meta:
        model = Company
        fields = ('name', 'industry', 'created_at', 'created_by', 'tokens')
    
    def create(self, validated_data):
        company = Company(
            name=validated_data['name'],
            industry=validated_data['industry'],
            created_by=self.request.user
        )
        company.save()    
        return company

class EmployeeSerializer(serializers.ModelSerializer):
    """Serializer for register employee objects."""
    tokens = serializers.SerializerMethodField()

    class Meta:
        fields = ('username', 'email', 'user_type', 'tokens')
        model = User

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()    
        return user
